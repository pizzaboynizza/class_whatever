# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
# from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

class IndexView(generic.ListView):
  template_name = 'polls/index.html'
  context_object_name = 'latest_question_list'

  def get_queryset(self):
    return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
  model = Question
  template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
  model = Question
  template_name = 'polls/results.html'

# def index(request):
#   latest_question_list = Question.objects.order_by('-pub_date')[:5]
#   # template = loader.get_template('polls/index.html')
#   context = {
#     'latest_question_list': latest_question_list
#   }
#   return render(request, 'polls/index.html', context)

# def detail(request, question_id):
#   question = get_object_or_404(Question, pk=question_id)
#   return render(request, 'polls/detail.html', {'question': question})

# def results(request, question_id):
#   # return HttpResponse(f"You're looking at the results of question {question_id}.")
#   question = get_object_or_404(Question, pk=question_id)
#   return render(request, 'polls/results.html', {'question': question})
#   # return HttpResponseRedirect('polls/results.html')

def vote(request, question_id):
  # return HttpResponse(f"You're voting on question {question_id}.")
  question = get_object_or_404(Question, pk=question_id)
  try:
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
  except (KeyError, Choice.DoesNotExist):
    return render(request, 'polls/detail.html', {'question': question, 'error_message': "You didn't select a choice."})
  else:
    selected_choice.votes += 1
    selected_choice.save()
    # return HttpResponseRedirect(f"/polls/{question.id}/results/")
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# def status_page(request):
# print("Inside redirect")
# return HttpResponseRedirect(request,'my_app/status.html')

# In your views.py, HttpResponseRedirect is used incorrectly. If you want to redirect to a new page, then you should use,

# return HttpResponseRedirect('/url-where-you-want-to-redirect/')