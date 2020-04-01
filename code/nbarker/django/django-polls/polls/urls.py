from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), # /polls/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'), # /polls/1/ or /polls/5/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'), # /polls/1/results/ or /polls/5/results/
    path('<int:question_id>/vote', views.vote, name='vote') # /polls/1/vote/ or /polls/5/vote/
]

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('<int:question_id>/', views.detail, name='detail'),
#     path('<int:question_id>/results/', views.results, name='results'),
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]