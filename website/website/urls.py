from django.contrib import admin
from django.urls import path
from website import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('feedback/', views.feedback),
    path('contact/', views.contact),
    path('about/', views.about),
    path('services/', views.services),
]
