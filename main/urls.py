from django.urls import include
from django.conf import Settings
from django.urls import *
from . import views
from .views import *
from django.urls import path
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('download/', views.download_cv, name='downloading'),
    path('contact/', views.contact_view, name='contact'),
]