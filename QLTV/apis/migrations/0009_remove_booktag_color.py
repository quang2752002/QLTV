# Generated by Django 5.1.3 on 2024-11-09 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0008_booktag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booktag',
            name='color',
        ),
    ]