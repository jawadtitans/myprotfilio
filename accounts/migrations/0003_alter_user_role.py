# Generated by Django 4.2 on 2025-06-19 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'admin'), (1, 'instructor'), (2, 'student')], null=True),
        ),
    ]
