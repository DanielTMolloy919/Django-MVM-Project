# Generated by Django 3.2 on 2021-11-10 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0002_alter_vendor_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='slug',
            field=models.SlugField(default='djangodbmodelsfieldscharfield', max_length=255),
        ),
    ]
