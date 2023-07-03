# Generated by Django 4.1.5 on 2023-07-03 05:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="description",
            field=models.CharField(default=django.utils.timezone.now, max_length=1500),
            preserve_default=False,
        ),
    ]
