# Generated by Django 3.2 on 2021-12-07 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0003_vendor_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='g_rating',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='g_review_count',
            field=models.IntegerField(default=0),
        ),
    ]