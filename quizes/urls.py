# -*- coding: utf-8 -*-
from django.urls import path
from .views import  *

app_name = 'quizes'

urlpatterns = [
    path('', quiz_list, name='main-view'),
    path('<int:pk>/', quiz_view, name='quiz-view'),
    path('<pk>/save/', save_quiz_view, name='save-view'),
    path('<pk>/data/', quiz_data_view, name='quiz-data-view'),
    path('login/', MyprojectLoginView.as_view(), name='login_page'),
    path('register/', RegisterUserView.as_view(), name='register_page'),
    path('logout/', MyProjectLogout.as_view(), name='logout_page'),
]