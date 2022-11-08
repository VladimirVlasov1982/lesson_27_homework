# Generated by Django 4.1.3 on 2022-11-07 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ads",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=200)),
                ("author", models.CharField(max_length=150)),
                ("price", models.IntegerField()),
                ("description", models.CharField(max_length=2000)),
                ("address", models.CharField(max_length=100)),
                ("is_published", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="Categories",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=300)),
            ],
        ),
    ]
