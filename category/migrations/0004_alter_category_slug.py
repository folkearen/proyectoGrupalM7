# Generated by Django 4.2.4 on 2023-08-22 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
