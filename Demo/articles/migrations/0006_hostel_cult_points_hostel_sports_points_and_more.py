# Generated by Django 4.2.4 on 2023-08-29 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_alter_hostel_total_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostel',
            name='Cult_Points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hostel',
            name='Sports_Points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hostel',
            name='Tech_Points',
            field=models.IntegerField(default=0),
        ),
    ]
