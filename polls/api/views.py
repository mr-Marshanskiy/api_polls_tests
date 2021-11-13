from datetime import datetime

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.serializers import ValidationError

from .models import Poll, Question, User
from .permissions import IsAdminOrReadOnly
from .serializers import (AnswerSerializer, ChoiceSerializer,
                          CompletedPollsSerializer, PollSerializer,
                          QuestionSerializer, UserSerializer)


class PollViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    @action(detail=False, url_path='active-polls')
    def active_polls(self, request):
        polls = Poll.objects.filter(end_date__gte=datetime.now())
        serializer = self.get_serializer(polls, many=True)
        return Response(serializer.data)


class QuestionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = QuestionSerializer

    def get_queryset(self):
        pool = get_object_or_404(Poll, id=self.kwargs.get('poll_id'))
        return pool.questions.all()

    def perform_create(self, serializer):
        serializer.save(poll=get_object_or_404(
            Poll,
            id=self.kwargs.get('poll_id'))
        )


class ChoiceViewSet(viewsets.ModelViewSet):
    serializer_class = ChoiceSerializer

    def get_queryset(self):
        question = get_object_or_404(Question,
                                     id=self.kwargs.get('question_id'))
        return question.choices.all()

    def perform_create(self, serializer):
        serializer.save(question=get_object_or_404(
            Question,
            id=self.kwargs.get('question_id'))
        )


class AnswerViewSet(viewsets.ModelViewSet):
    serializer_class = AnswerSerializer

    def get_queryset(self):
        question = get_object_or_404(Question,
                                     id=self.kwargs.get('question_id'))
        return question.answers.all()

    def perform_create(self, serializer):
        question = get_object_or_404(Question,
                                     id=self.kwargs.get('question_id'))
        user = serializer.validated_data['user_id']
        if user.answers.filter(question=question.id).exists():
            raise ValidationError('Пользователь уже ответил на вопрос')
        if (question.type == 0
                and serializer.validated_data['text'] is None):
            raise ValidationError('Это развернутый ответ. Впишите ответ')
        if (question.type == 1
                and len(serializer.validated_data['choice']) != 1):
            raise ValidationError('Выберите один ответ')
        if (question.type == 2
                and len(serializer.validated_data['choice']) == 0):
            raise ValidationError('Выберите хотя бы один ответ')

        choices = serializer.validated_data['choice']
        text = serializer.validated_data['text']
        if question.type == 0:
            choices = []
        else:
            text = ''
        serializer.save(
            question=get_object_or_404(Question,
                                       id=self.kwargs.get('question_id')),
            choices=choices,
            text=text
        )


class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class CompletedPollsViewSet(viewsets.ModelViewSet):
    serializer_class = CompletedPollsSerializer

    def get_queryset(self):
        user = get_object_or_404(User, id=self.kwargs.get('user_id'))
        print(user)
        answers = user.answers.all()
        questions = Question.objects.filter(id__in=answers)
        polls = Poll.objects.filter(id__in=questions).distinct()

        return polls
