from django.db import models
from django.utils import timezone


class Travel(models.Model):
    site_id = models.CharField(max_length=100, blank=True, null=True)
    added = models.DateTimeField(default=timezone.now, blank=True, null=True)
    price = models.CharField(max_length=50, default='PLN', blank=True, null=True)
    place = models.CharField(max_length=100, default='place', blank=True, null=True)
    img_link = models.TextField(max_length=500)
    title = models.CharField(max_length=200, default='title', blank=True, null=True)
    title2 = models.TextField(blank=True, null=True)
    address = models.TextField(default='address', blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    summary_cont = models.TextField(blank=True, null=True)
    promo_dates = models.CharField(max_length=100, blank=True, null=True)
    promo_price = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'Travel {self.site_id}, {self.pk}'
