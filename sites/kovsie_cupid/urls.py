
from . import views
from django.urls import path


urlspatterns = [
    path('', views.loading_page, name='loading_page'),

]