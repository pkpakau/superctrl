from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth

urlpatterns=[
    
    url(r'^dashboard/',views.dashboard,name="dashboard"),
]