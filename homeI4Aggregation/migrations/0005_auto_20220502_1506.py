# Generated by Django 3.2.13 on 2022-05-02 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homeI4Aggregation', '0004_makelist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inhouseinventory',
            name='description',
        ),
        migrations.RemoveField(
            model_name='inhouseinventory',
            name='dimension',
        ),
    ]