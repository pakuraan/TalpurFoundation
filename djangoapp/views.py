from django.shortcuts import render

def index(request):
    return render(request,'home.html')

def history(request):
    return render(request,'history.html')

def leadership(request):
    return render(request,'leadership.html')

def sites(request):
    return render(request,'sites.html')

