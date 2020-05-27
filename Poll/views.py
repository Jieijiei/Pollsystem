from django.shortcuts import render
from .models import Work
from django.views.generic import ListView


class WorkList(ListView):
    context_object_name = 'object_list'
    model = Work
# Create your views here.
