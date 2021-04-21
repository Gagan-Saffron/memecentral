from django.contrib import admin
from django.urls import path

from .views import home_view,cricket_view,engineering_view

urlpatterns = [
	path('',home_view,name='home'),
	path('cricket/',cricket_view,name='cricket'),
	path('engineering/',engineering_view,name='engineering')
]