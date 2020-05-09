
from django.shortcuts import render
import requests
import os

def button(request):

    return render(request,'home.html')

def output(request):
    os.system('ping 8.8.8.8')

print (os.system)
