from django.shortcuts import render
from .models import Quiz, OX_Quiz
from django.db.models import Q
from django.shortcuts import render


def index(request):

    return render(request, 'index.html')


def quiz(request):
    quiz = Quiz.objects.order_by('?')[0]
    context = {"quiz": quiz}

    return render(request, 'quiz.html', context)


def result(request):
    q = request.GET['user_answer']
    a = request.GET['answer']
    flag = "플래그"

    if a == q:
        flag = "정답입니다"
        context = {"flag": flag}

        return render(request, 'result.html', context)
    else:
        flag = "틀렸습니다"
        context = {"flag": flag}
        context['mean'] = a
        return render(request, 'result.html', context)


def ox_quiz(request):
    ox_quiz = OX_Quiz.objects.order_by('?')[0]
    context = {"ox_quiz": ox_quiz}

    return render(request, 'ox_quiz.html', context)


def ox_result(request):
    q = request.GET['user_answer']
    a = request.GET['answer']
    ex = request.GET['ex']
    flag = "플래그"

    if a == q:
        flag = "정답입니다"
        context = {"flag": flag}

        return render(request, 'ox_result.html', context)
    else:
        flag = "틀렸습니다"
        context = {"flag": flag}
        context['ex'] = ex
        return render(request, 'ox_result.html', context)
