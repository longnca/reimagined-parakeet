# Generated by Django 5.0.3 on 2024-03-17 20:39

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PredResults",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("previous_day_pool_price", models.FloatField()),
                ("mean_temp", models.FloatField()),
                ("rolling_30day_avg", models.FloatField()),
                ("alberta_internal_load", models.FloatField()),
                ("ng_price", models.FloatField()),
                ("spd_of_max_gust", models.FloatField()),
                ("day_of_year", models.FloatField()),
                ("total_precip", models.FloatField()),
                ("is_public_holiday", models.FloatField()),
                ("pool_price", models.FloatField()),
            ],
        ),
    ]
