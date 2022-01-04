# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import lecture,attendance_report,supportQueries,deployment_model

# Register your models here.
class ModelAdminLecture(admin.ModelAdmin):
    list_display = ('id','name','teacher_name','link','desc')

class ModelAdminAttendance(admin.ModelAdmin):
    list_display = ('id','username','name','date','value','initial_date')

class ModelAdminQueries(admin.ModelAdmin):
    list_display = ('id','username','typeOfQuery','date','problemDesc','value')

class ModelAdminDeployedModel(admin.ModelAdmin):
    list_display = ('id','project_name','username','link','backend_technology','frontend_technology','database_used','desc','date')    

admin.site.register(lecture,ModelAdminLecture)
admin.site.register(attendance_report,ModelAdminAttendance)
admin.site.register(supportQueries,ModelAdminQueries)
admin.site.register(deployment_model,ModelAdminDeployedModel)