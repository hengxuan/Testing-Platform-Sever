from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from User_App.user_views import *

urlpatterns = [
    path('register/',Api_register.as_view()),
    path('login/',Api_login.as_view()),
    path('update/',Api_resetpassword.as_view()),
    path('delete/',Api_del.as_view()),
    path('test/',Api_test.as_view())

]