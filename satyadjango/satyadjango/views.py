from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render (request,'index.html')
   

def about(request):
    return HttpResponse ("this is about page")

def contact (request):
    return HttpResponse("this is contact us page ")