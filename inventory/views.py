from django.http import HttpResponse
from django.shortcuts import redirect, render

def home_view(request):
    return render(request, "home.html")