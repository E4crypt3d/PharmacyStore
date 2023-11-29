from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from store.models import Sale, Notification
from django.core.paginator import Paginator
from django.contrib.auth import logout as logout_user
from django.contrib.auth import login as login_user
from django.core.exceptions import PermissionDenied
from django.contrib.auth import authenticate
from django.db.models import Sum
from django.utils import timezone
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool, NumeralTickFormatter
from bokeh.transform import factor_cmap
from bokeh.palettes import Category20
from bokeh.embed import components
import calendar

# Create your views here.


@login_required
def home(request):
    try:
        sales = Sale.objects.select_related('user').all()
        current_year = timezone.now().year
        current_month = timezone.now().month

        sales_data = Sale.objects.filter(added_at__year=current_year).values(
            'added_at__month').annotate(total_sales=Sum('total_amount'))
        sales_dict = {i: {"added_at__month": i, "total_sales": 0}
                      for i in range(1, current_month + 1)}
        for entry in sales_data:
            month = entry['added_at__month']
            sales_dict[month] = {"added_at__month": month,
                                 "total_sales": entry['total_sales']}
        # Finding the avg of current and previous month and comparing their performances
        cmonth = sales_dict[current_month]['total_sales']
        pmonth = sales_dict[current_month-1]['total_sales']
        cmonth_percent = cmonth / (cmonth + pmonth) * 100
        pmonth_percent = pmonth / (pmonth + cmonth) * 100
        performance = cmonth_percent - pmonth_percent

        months = [calendar.month_name[sales_dict[entry]['added_at__month']]
                  for entry in sales_dict]
        total_sales_amounts = [sales_dict[entry]
                               ['total_sales'] for entry in sales_dict]

        p = figure(x_range=[str(month) for month in months], title=f'Sales Amount in {current_year} by Month',
                   toolbar_location=None, tools="", sizing_mode='stretch_width')

        # Create a ColumnDataSource with the sales data
        source = ColumnDataSource(data=dict(
            months=[str(month) for month in months], total_sales=total_sales_amounts))

        # Add bar glyphs to the figure
        p.vbar(x='months', top='total_sales', width=1, source=source, line_color="white", fill_color=factor_cmap(
            'months', palette=Category20[12], factors=[str(month) for month in months]))
        hover = HoverTool(
            tooltips=[("Month", "@months"), ("Total Sales", "@total_sales")])
        # Customize the plot
        p.add_tools(hover)
        p.y_range.start = 0
        p.yaxis[0].formatter = NumeralTickFormatter(format="Rs0.0a")

        # Generate Bokeh script and div components
        script, div = components(p)

        total_amount = sum([i.total_amount for i in sales])
        total_products = sales.values('product').distinct().count
        recent_sales = sales.order_by('-added_at')[:10]
        notified_notifications = Notification.notified.all()
        context = {'products': total_products,
                   'total_amount': total_amount,
                   'sales': recent_sales,
                   'notified': notified_notifications,
                   'script': script, 'div': div,
                   'performance': int(performance)}
        return render(request, 'index.html', context)
    except Exception as e:
        return HttpResponseNotFound()


@login_required
def sales(request):
    try:
        q = request.GET.get('q', False)
        page_number = request.GET.get("page")
        sorted_by = request.session.get('order_by', False)
        if q:
            sales = Sale.objects.select_related(
                'user').filter(product__icontains=q)
            sales_count = sales.count()
        else:
            if sorted_by:
                sales = Sale.objects.select_related(
                    'user').all().order_by(sorted_by)
            else:
                sales = Sale.objects.select_related('user').all()
            sales_count = sales.count()
        notified = Notification.notified.all()
        paginated_sales = Paginator(sales, 20)
        page_obj = paginated_sales.get_page(page_number)
        context = {'sales': page_obj,
                   'notified': notified,
                   'sales_count': sales_count}
        return render(request, 'sales.html', context)
    except Exception as e:
        return redirect('sales')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')
        user = authenticate(username=username, password=password)
        if user:
            login_user(request, user)
            if not remember:
                request.session.set_expiry(0)
        return redirect('home')
    return render(request, 'login.html')


def sort_products(request):
    try:
        sort = request.GET.get('o', False)
        page = request.GET.get('page', False)
        a = request.session.get('sort', False)
        value_check = {
            '0': ['product', '-product'],
            '1': ['price', '-price'],
            '2': ['quantity', '-quantity'],
            '3': ['total_amount', '-total_amount'],
            '4': ['user', '-user'],
            '5': ['added_at', '-added_at'],
            '6': ['modified_at', '-modified_at']
        }
        sort_by = value_check.get(sort, False)

        if sort == a:
            sort_by = sort_by[1]
            request.session['sort'] = f'-{sort}'
            request.session['order_by'] = sort_by
        else:
            sort_by = sort_by[0]
            request.session['sort'] = sort
            request.session['order_by'] = sort_by

        if sort and sort_by:
            sorted = Sale.objects.select_related(
                'user').all().order_by(sort_by)
            sales_count = sorted.count()
            if not page:
                if page == "":
                    page = '1'
            paginator = Paginator(sorted, 20)
            sorted = paginator.get_page(page)
            context = {'sales': sorted, 'sales_count': sales_count}
        else:
            return HttpResponseNotFound()
        return render(request, 'partials/salestable.html', context)
    except Exception as e:
        return HttpResponseNotFound()


def logout(request):
    try:
        if request.user.is_authenticated:
            logout_user(request)
            return redirect('home')
        else:
            raise PermissionDenied("User not authenticated")
    except Exception as e:
        return HttpResponseNotFound()
