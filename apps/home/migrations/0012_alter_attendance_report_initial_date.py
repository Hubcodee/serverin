# Generated by Django 3.2.7 on 2021-12-27 12:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_attendance_report_initial_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance_report',
            name='initial_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 27, 18, 21, 53, 754329), null=True),
        ),
    ]
