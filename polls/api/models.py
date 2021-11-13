from django.contrib.auth import get_user_model
from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=15, null=True,
                                  verbose_name='Имя')
    last_name = models.CharField(max_length=20, null=True,
                                 verbose_name='Фамилия')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        if self.first_name or self.last_name:
            return f'{self.first_name} {self.last_name}'
        return str(self.id)


class Poll(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название опроса')
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name='Начало опроса')
    end_date = models.DateTimeField(verbose_name='Окончание опроса')
    description = models.TextField(verbose_name='Описание опроса')

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    def __str__(self):
        return self.name


class Question(models.Model):
    poll = models.ForeignKey(Poll, related_name='questions',
                             on_delete=models.CASCADE,
                             verbose_name='Опрос',)
    content = models.CharField(max_length=150,
                               verbose_name='Название вопроса')
    type = models.SmallIntegerField(verbose_name='Тип вопроса')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.content


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices',
                                 on_delete=models.CASCADE,
                                 verbose_name='Вопрос')
    text = models.CharField(max_length=150, verbose_name='Вариант ответа')

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'

    def __str__(self):
        return self.text


class Answer(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name='answers',
                                verbose_name='Пользователь')
    question = models.ForeignKey(Question, related_name='answers',
                                 on_delete=models.CASCADE,
                                 verbose_name='Вопрос')
    choice = models.ManyToManyField(Choice, related_name='answers',
                                    null=True, blank=True,
                                    verbose_name='Вариант ответа')
    text = models.CharField(max_length=150, null=True, verbose_name='Ответ')

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return self.text
