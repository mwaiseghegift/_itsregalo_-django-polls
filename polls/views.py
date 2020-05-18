from django.shortcuts import render, get_object_or_404
from .models import Question,Choice
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.views.generic import (ListView,TemplateView,DetailView)


# Create your views here
#function view
"""
#get questions and desplay them

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


# show specific questions and choices
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', { 'question':question })


# get question and desplay results

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question})
"""

#class based view

class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]
        
class DetailView(DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        #below is the selected choice
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        # request.POST['choice'] will raise KeyError if choice wasn’t provided in POST data.
    except(KeyError, choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question':question,
                                                    'error_message': "You didn't select a choice."})

    else:
        selected_choice.votes +=1
        selected_choice.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))