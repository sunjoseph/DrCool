from django.shortcuts import render
import requests

def homepage(request):
    return render(request, 'web/homepage.html')

# def appliances(request):
#     return render(request, 'web/appliances.html')   

