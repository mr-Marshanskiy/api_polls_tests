from datetime import datetime

import pytz
from rest_framework import serializers

from .models import Answer, Choice, Poll, Question, User


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ('id', 'name', 'pub_date', 'end_date', 'description')

    def validate_end_date(self, value):
        now = datetime.utcnow().replace(tzinfo=pytz.UTC)
        if now > value:
            raise serializers.ValidationError(
                'Время окончания должно быть больше текущего времени')
        return value


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'content', 'type')

    def validate_type(self, value):
        if int(value) in range(3):
            return value
        raise serializers.ValidationError(
            'Введите корректный тип вопроса: 0(текст), 1(выбор одного) или 2'
            '(множественный выбор)')


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'text')


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'user_id', 'choice', 'text')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')


class CompletedQuestionsSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(read_only=True, many=True)

    class Meta:
        model = Question
        fields = ('content', 'answers')


class CompletedPollsSerializer(serializers.ModelSerializer):
    questions = CompletedQuestionsSerializer(read_only=True, many=True)

    class Meta:
        model = Poll
        fields = ('id', 'name', 'pub_date', 'end_date',
                  'description', 'questions')
