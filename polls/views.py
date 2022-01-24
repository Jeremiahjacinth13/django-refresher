from django.http import HttpResponse
from django.shortcuts import render

from .models import Question

def index(request):
    last_five_questions = Question.objects.order_by('-pub_date')[:5]
    context = {'last_five_questions': last_five_questions}
    return render(request, 'polls/index.html', context = context)

def detail(request, question_id):
    try:
        question = Question.objects.get(id = question_id)
    except Question.DoesNotExist:
        return HttpResponse('Question %s does not exist' % question_id)
    return render(request, 'polls/details.html', { 'question': question })
    

def results(request, question_id):
    return HttpResponse('You are looking at the results of question %s.' % question_id)

def vote(request, question_id):
    return HttpResponse('You are voting on question %s.' % question_id)