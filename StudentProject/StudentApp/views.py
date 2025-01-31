from django.shortcuts import render
from .models import Student
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "web/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["student"] = Student.objects.all()
        return context
