from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def doc(request):
    return render(request, 'doc.html')