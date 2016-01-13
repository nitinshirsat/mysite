from django.http import HttpResponse
from django.template import loader

from models import Question, Choice

# Create your views here.

def index(request):

    my_latest_questions = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'my_latest_questions_inside_template': my_latest_questions,
    }
    return HttpResponse(template.render(context, request))

def about_us(request):
    return HttpResponse("I have created this site, My name is Nitin")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)