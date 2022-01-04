# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class lecture(models.Model):
    name = models.CharField(max_length=120)
    teacher_name = models.CharField(max_length=40)
    desc = models.CharField(max_length=200)
    link = models.CharField(max_length=50)
    username = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    
    def __str__(self):
        return self.name
    
    class Meta:
      db_table = "Lecture"
      verbose_name = "Lecture"
      verbose_name_plural = "Lectures"

class attendance_report(models.Model):
    initial_date = models.DateTimeField(auto_now_add=False,default=datetime.now(),blank=True)
    date = models.DateTimeField(auto_now_add=True)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.ForeignKey(lecture,on_delete=models.CASCADE)
    value = models.IntegerField(default=1)

    class Meta:
      db_table = "Attendance Report"
      verbose_name = "Attendance Report"
      verbose_name_plural = "Attendance Reports"

    def __str__(self):
        return str(self.username)
    
class deployment_model(models.Model):
    project_name = models.CharField(max_length=20)
    desc = models.CharField(max_length=200)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    backend_technology = models.CharField(max_length=20)
    frontend_technology = models.CharField(max_length=20)
    database_used = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    link = models.URLField(max_length=100)

    class Meta:
      db_table = "Deployment Model"
      verbose_name = "Deployment Model"
      verbose_name_plural = "Deployment Models"

    def __str__(self):
        return self.project_name  

status_choice = (("Open","Open"), ("Closed","Closed"),)
query_choice = (("Technical","Technical"), ("Service Usage","Service Usage"),("Feedback/Suggestion","Feedback/Suggestion"))

class supportQueries(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    typeOfQuery = models.CharField(max_length=20,choices=query_choice)
    date = models.DateTimeField(auto_now_add=True)
    problemDesc = models.CharField(max_length=300)
    value = models.CharField(max_length=10,default="Open",choices=status_choice)

    class Meta:
      verbose_name = "Support Query"
      verbose_name_plural = "Support Queries"
      db_table = "Support Query"

    def __str__(self):
        return str(self.username)  

    