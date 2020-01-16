# Generated by Django 3.0 on 2020-01-16 16:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_travel_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='added',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='travel',
            name='address',
            field=models.TextField(blank=True, default='address', null=True),
        ),
        migrations.AlterField(
            model_name='travel',
            name='place',
            field=models.CharField(blank=True, default='place', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='travel',
            name='price',
            field=models.CharField(blank=True, default='PLN', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='travel',
            name='title',
            field=models.CharField(blank=True, default='title', max_length=200, null=True),
        ),
    ]
