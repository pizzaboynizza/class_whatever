from django.shortcuts import get_object_or_404, render
from django.template import loader
from .models import Grocery_item
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# Create your views here.

'''views.py is how urls.py interact with this particular app'''

def index(request):
    context = {
        "incomplete_items": Grocery_item.objects.filter(is_completed= False),
        "complete_items": Grocery_item.objects.filter(is_completed = True)
    }
    return render(request, 'grocery_app/index.html', context)

def add(request):
    # this answer is generated from the input field in my form on index.html
    input_answer = request.POST['text_field']
    # its creating and adding whatever the user types in and adding it to the Grocery list and the time it was published
    Grocery_item.objects.create(grocery_item = input_answer, pub_date = timezone.now())
    # 
    return HttpResponseRedirect(reverse('grocery_app:index'))

def delete(request, grocery_id):
    grocery = get_object_or_404(Grocery_item, pk=grocery_id)
    grocery.delete()

    




# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {
#         'latest_question_list': latest_question_list
#     }
#     return render(request, 'polls/index.html', context)


# def detail(request, question_id):
#         question = get_object_or_404(Question, pk=question_id)
#         return render(request, 'polls/detail.html',{'question':question})


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
