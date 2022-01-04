# Generated by Django 3.2.7 on 2021-12-27 16:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20211227_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance_report',
            name='initial_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 27, 22, 19, 21, 809846)),
        ),
        migrations.AlterField(
            model_name='supportqueries',
            name='typeOfQuery',
            field=models.CharField(choices=[('Technical', 'Technical'), ('Service Usage', 'Service Usage'), ('Feedback/Suggestion', 'Feedback/Suggestion')], max_length=20),
        ),
    ]
