from django.shortcuts import render

# Create your views here.

def loading_page(request):
    return render(request, 'loading.html')
