from django.http import HttpResponse, Http404, HttpResponseRedirect
from models import Question, Choice
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone


class IndexView (generic.ListView):
    queryset = Question.objects.filter(pub_date__lte=timezone.now())order_by('-pub_date')[:5]
    context_object_name = 'my_latest_questions_inside_template'
    template_name = 'polls/index.html'


class DetailsView(generic.DetailView):
    model = Question
    template_name = 'polls/details.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/result.html'


def about_us(request):
    return HttpResponse("I have created this site, My name is Nitin")

"""
def results(request, question_id):
    question = get_object_or_404 (Question, pk=question_id )
    context = {'question': question, }

    return render(request, 'polls/result.html',context)
"""
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        if request.POST['choice'] is  None:
            raise KeyError
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))



