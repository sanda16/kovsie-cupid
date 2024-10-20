# kovsie_connections/views.py

from django.shortcuts import render

def loading_page(request):
    return render(request, 'accounts/loading.html')

def create_account_page(request):
    return render(request, 'accounts/create_account.html')
