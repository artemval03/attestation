# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import AuthUserForm, RegisterUserForm
from .models import Quiz, Teachers, VideoMaterials, FileMaterials
from django.views.generic import ListView, CreateView
from django.http import JsonResponse
from questions.models import Question, Answer
from results.models import Result


class RegisterUserView(CreateView):
    model = User
    template_name = 'quizes/register_page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('quizes:main-view')
    success_msg = 'Пользователь успешно создан'

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        aut_user = authenticate(username=username, password=password)
        login(self.request, aut_user)
        return form_valid


class MyProjectLogout(LogoutView):
    next_page = reverse_lazy('quizes:main-view')


def quiz_list(request):
    obj = Quiz.objects.all()
    teachers = Teachers.objects.all()
    videos = VideoMaterials.objects.all()
    files = FileMaterials.objects.all()
    template_name = 'quizes/main.html'

    context = {
        'teachers': teachers,
        'object_list': obj,
        'videos': videos,
        'files': files,
    }

    return render(request, template_name, context)


def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)

    return render(request, 'quizes/quiz.html', {'obj': quiz})


def quiz_data_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q): answers})
    return JsonResponse({
        'data': questions,
        'time': quiz.time,
    })


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def save_quiz_view(request, pk):
    if is_ajax(request=request):
        questions = []
        data = request.POST
        data_ = dict(data.lists())

        data_.pop('csrfmiddlewaretoken')

        for k in data_.keys():
            print('key: ', k)
            question = Question.objects.get(text=k)
            questions.append(question)
        print(questions)

        user = request.user
        quiz = Quiz.objects.get(pk=pk)

        score = 0
        multiplier = 100 / quiz.number_of_questions
        results = []
        correct_answer = None

        for q in questions:
            a_selected = request.POST.get(q.text)

            if a_selected != "":
                question_answers = Answer.objects.filter(question=q)
                for a in question_answers:
                    if a_selected == a.text:
                        if a.correct:
                            score += 1
                            correct_answer = a.text
                    else:
                        if a.correct:
                            correct_answer = a.text

                results.append({str(q): {'correct_answer': correct_answer, 'answered': a_selected}})
            else:
                results.append({str(q): 'нет ответа'})

        score_ = score * multiplier
        Result.objects.create(quiz=quiz, user=user, score=score_)

        if score_ >= quiz.required_score_to_pass:
            return JsonResponse({'passed': True, 'score': score_, 'results': results})
        else:
            return JsonResponse({'passed': False, 'score': score_, 'results': results})


class MyprojectLoginView(LoginView):
    template_name = 'quizes/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('quizes:main-view')

    def get_success_url(self):
        return self.success_url


