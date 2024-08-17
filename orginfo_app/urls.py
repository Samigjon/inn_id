from django.urls import path
from . import views

urlpatterns = [
    path('', views.org_info_view, name='org_info'),
]