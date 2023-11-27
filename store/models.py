from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timesince import timesince
from django.utils import timezone
# Create your models here.


class User(AbstractUser):
    pass


class Sale(models.Model):
    product = models.CharField(max_length=130)
    quantity = models.IntegerField()
    price = models.PositiveBigIntegerField()
    added_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    total_amount = models.IntegerField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="sold", blank=True)

    class Meta:
        ordering = ['-modified_at']

    def save(self, *args, **kwargs):
        if self.quantity and self.price:
            self.total_amount = self.quantity * self.price
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.product

    @property
    def time_since_modified(self):
        now = timezone.now()
        return f"{timesince(self.modified_at, now)} ago"

# Notfications


class NotificationManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_notified=True)


class Notification(models.Model):
    objects = models.Manager()
    notified = NotificationManager()
    notification_types = [
        ("red", "Urgent"),
        ("blue", "General"),
        ("green", "Success")
    ]
    notification_type = models.CharField(
        choices=notification_types, max_length=10)
    notification_msg = models.CharField(max_length=280)
    is_notified = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.is_notified:
            Notification.objects.exclude(id=self.id).update(is_notified=False)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.notification_msg
