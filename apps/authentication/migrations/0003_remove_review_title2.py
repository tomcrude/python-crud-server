# Generated by Django 4.2 on 2023-04-18 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_review_title2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='title2',
        ),
    ]
