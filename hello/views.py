from django.shortcuts import render
from django.http import HttpResponse
from .models import Jobs

# Register your models here.

admin.site.register(Jobs)
