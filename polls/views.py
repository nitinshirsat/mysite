from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hi there, welcome to poll application")

def about_us(request):
    return HttpResponse("I have created this site, My name is Nitin")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)