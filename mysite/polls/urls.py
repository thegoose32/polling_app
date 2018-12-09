from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('newQuestion', views.newQuestion, name='newQuestion'),
    path('<int:pk>/newAnswer/', views.newAnswerFormView.as_view(), name='newAnswerForm'),

    #DG - is there a more efficent way to handle these functions?
    path('<int:question_id>/deleteQuestion', views.deleteQuestion, name='deleteQuestion'),
    path('new_question', views.newQuestionForm, name='new_question'),
    path('<int:question_id>/newAnswerSubmit/', views.newAnswerSubmit, name='newAnswerSubmit'),
    path('<int:choice_id>/deleteAnswer', views.deleteAnswer, name='deleteAnswer'),
]
