# kovsie_connections/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.loading_page, name='loading_page'),
    path('create_account/', views.create_account_page, name='create_account_page'),
]
