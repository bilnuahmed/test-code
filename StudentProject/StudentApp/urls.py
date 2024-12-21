from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
]
