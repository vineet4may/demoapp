from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from DemoApp import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
]
