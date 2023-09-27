#!/usr/bin/env python
__author__ = "Ryan Belanger"
from django.urls import path
from .views import homePageView

urlpatterns = [
    path("",homePageView,name="home"),

]