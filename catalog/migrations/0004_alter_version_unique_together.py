# Generated by Django 4.2.7 on 2023-12-23 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_version'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='version',
            unique_together={('number', 'product')},
        ),
    ]
