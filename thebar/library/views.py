from django.shortcuts import render
from.models import Question, Answer

def home(request):
    context = {
        'questions': Question.objects.all(),
        'answers': Answer.objects.all(),
    }
    return render(request, 'library/home.html', context)

def about(request):
    return render(request, 'library/about.html')