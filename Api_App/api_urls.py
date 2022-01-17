from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from Api_App.api_views import *

urlpatterns = [
    path('get_response/',Api_action.as_view()),

]