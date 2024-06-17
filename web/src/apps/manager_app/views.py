from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def clients(request):
    return HttpResponse('This is clients page')

def work(request):
    return HttpResponse('This is work page')

def materials(request):
    return HttpResponse('This is materials page')

def cars(request):
    return HttpResponse('This is cars page')

def work_types(request):
    return HttpResponse('This is work_types page')

def masters(request):
    return HttpResponse('This is masters page')

