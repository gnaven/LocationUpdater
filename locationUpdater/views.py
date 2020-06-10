from django.shortcuts import render
import requests
import sys
from subprocess import run,PIPE

def button (request):
    return render(request,'home.html')

def output (request):
    data =requests.get("https://reqres.in/api/users")
    print(data.text)
    data =data.text
    return render(request,'home.html',{'data1':data})

def external(request):
    
    out = run([sys.executable,'//Users/gnaven/OneDrive - University of Rochester/Full-Time/Dimagi/locationUpdater/LocationUpdate.py'],shell=False,stdout=PIPE)
    data = out.stdout.decode("utf-8")
    return render(request,'home.html',{'data1':data})
    