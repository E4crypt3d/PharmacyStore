from typing import Any
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from store.models import User, Sale, Notification

# Register your models here.
admin.site.register(User, UserAdmin)


@admin.register(Sale)
class AdminSale(admin.ModelAdmin):
    list_display = ['id', 'product', 'price',
                    'quantity', 'total_amount', 'time_since_modified', 'added_at',]
    list_display_links = ['id', 'product', 'price',
                          'quantity', 'total_amount', 'time_since_modified', 'added_at',]
    search_fields = ['product']
    readonly_fields = ['total_amount', 'user']

    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        if not hasattr(obj, 'user'):
            obj.user = request.user
        return super().save_model(request, obj, form, change)


@admin.register(Notification)
class AdminNotification(admin.ModelAdmin):
    list_display = ['id', 'notification_type',
                    'notification_msg', 'is_notified']
    list_display_links = ['id', 'notification_type',
                          'notification_msg', 'is_notified']
