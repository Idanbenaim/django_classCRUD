# Generated by Django 4.1.7 on 2023-03-05 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="students",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="Posted_Images"),
        ),
    ]
