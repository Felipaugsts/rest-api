from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jobs/', views.JobList),
    path('jobs/<int:pk>', views.JobList)
]
