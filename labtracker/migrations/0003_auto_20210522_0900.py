# Generated by Django 2.2.16 on 2021-05-22 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labtracker', '0002_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
