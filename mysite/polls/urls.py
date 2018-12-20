from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('newQuestion', views.newQuestion, name='newQuestion'),
    path('<int:pk>/newAnswer/', views.newAnswerFormView.as_view(), name='newAnswerForm'),
    path('department', views.DeptView.as_view(), name='department'),
    path('<int:dept_id>/deleteDept', views.deleteDept, name='deleteDept'),
    path('<int:pk>/editDept', views.DeptUpdate.as_view(), name='editDept'),

    #DG - is there a more efficent way to handle these functions?
    path('<int:question_id>/deleteQuestion', views.deleteQuestion, name='deleteQuestion'),
    path('new_question', views.newQuestionForm, name='new_question'),
    path('<int:question_id>/newAnswerSubmit/', views.newAnswerSubmit, name='newAnswerSubmit'),
    path('<int:choice_id>/deleteAnswer', views.deleteAnswer, name='deleteAnswer'),
    path('new_department', views.createDept, name='new_department'),
]
