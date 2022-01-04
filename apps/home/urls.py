# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('lectures',views.lectures,name='lectures'),
    path('<int:pk>',views.remove,name='remove'),
    path('<int:pk>/attendance',views.attendance,name='attendance'),
    path('code_deployer',views.cd,name='code_deployer'),
    path('dev_space',views.dspace,name='dev_space'),
    path('ml',views.ml,name='ml'),
    path('security_playground',views.sp,name='sp'),
    path('add_lecture',views.add_lecture,name='add_lecture'),
    path('support',views.support,name='support'),
    path('profile',views.profile,name='profile'),
    path('developers',views.devs,name='developers'),
    path('documentation',views.docs,name='docs'),
    path('about_us',views.about,name='about'),


    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
