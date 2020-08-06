from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def motto(request):
    return HttpResponse("<h1> Heart of the Image </h1>")

def main(request):
    return render(request,"main.html")

def home(request):
    return render(request,"myapp/home.html")

def profile(request):
    name="Sunil Kumar"
    return render(request,"myapp/profile.html",{"name":name})