from django.urls import include, path
from rest_framework import routers

from . import views

polls = r'polls/(?P<poll_id>\d+)'
questions = r'questions/(?P<question_id>\d+)'
choices = r'choices/(?P<choice_id>\d+)'
users = r'users/(?P<user_id>\d+)'

router = routers.DefaultRouter()
router.register(r'polls', views.PollViewSet, basename='polls')
router.register(f'{polls}/questions',
                views.QuestionViewSet, basename='questions')
router.register(f'{polls}/{questions}/choices',
                views.ChoiceViewSet, basename='choices')
router.register(f'{polls}/{questions}/answers',
                views.AnswerViewSet, basename='answers')
router.register(r'users', views.UsersViewSet, basename='users')
router.register(f'{users}/completed_polls', views.CompletedPollsViewSet,
                basename='completed_polls')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
