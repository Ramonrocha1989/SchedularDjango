# Generated by Django 5.1.4 on 2025-01-29 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_category_contact_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.RemoveField(
            model_name='category',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='category',
            name='show',
        ),
    ]
