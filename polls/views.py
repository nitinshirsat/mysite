from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hi there, welcome to poll application")

def about_us(request):
    return HttpResponse("I have created this site, My name is Nitin")
