# yourapp/management/commands/generate_dummy_data.py

from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from store.models import Sale
import datetime


class Command(BaseCommand):
    help = 'Generates dummy data for testing'

    def handle(self, *args, **options):
        fake = Faker()

        for _ in range(100):
            start_date = timezone.now() - datetime.timedelta(days=500)
            end_date = timezone.now() - datetime.timedelta(days=150)
            print(fake.date_time_between(
                start_date='-500d', end_date='-150d'))
            Sale.objects.create(
                product=fake.word(),
                quantity=fake.random_int(min=1, max=100),
                price=fake.random_int(min=1, max=1000),
                added_at=fake.date_time_between(
                    start_date=start_date, end_date=end_date),
                # Assuming you have users with IDs 1 to 10
                user_id=fake.random_int(min=1, max=1)
            )

        self.stdout.write(self.style.SUCCESS(
            'Dummy data created successfully.'))
