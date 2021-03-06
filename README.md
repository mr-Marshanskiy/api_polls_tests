Тестовый проект API Polls предназначен для проведения опросов
### Функционал для администратора системы:

- авторизация в системе (регистрация не нужна)
- добавление/изменение/удаление опросов. Атрибуты опроса: название, дата старта, дата окончания, описание. После создания поле "дата старта" у опроса менять нельзя
- добавление/изменение/удаление вопросов в опросе. Атрибуты вопросов: текст вопроса, тип вопроса (ответ текстом, ответ с выбором одного варианта, ответ с выбором нескольких вариантов)

### Функционал для пользователей системы:

- получение списка активных опросов
- прохождение опроса: опросы можно проходить анонимно, в качестве идентификатора пользователя в API передаётся числовой ID, по которому сохраняются ответы пользователя на вопросы; один пользователь может участвовать в любом количестве опросов
- получение пройденных пользователем опросов с детализацией по ответам (что выбрано) по ID уникальному пользователя

## Использованные технологии

- Django 2.2.10
- Django REST framework.

## Процедура запуска проекта

**1. Клонировать репозиторий:**

git clone https://github.com/mr-Marshanskiy/api_polls_tests.git

**2. Перейти в директорию polls**

**3. Cоздать и активировать виртуальное окружение:**

python3 -m venv venv
source venv/Scripts/activate

**4. Установить зависимости из файла requirements.txt:**

pip install -r requirements.txt

**5. Выполнить миграции**

python manage.py makemigrations
python manage.py migrate

**6. Создать суперпользователя**

python manage.py createsuperuser

**7. Запустить приложение**

python manage.py runserver

## Взаимодействие с приложением

Корневой эндпоинт http://127.0.0.1:8000/api/

CRUD для опросов **polls/**

_Пример : http://127.0.0.1:8000/api/polls/_

CRUD отдельного **опроса polls/[id опроса]**

_Пример : http://127.0.0.1:8000/api/polls/1/_

Просмотр активных опросов 

_http://127.0.0.1:8000/api/polls/active-polls/_

CRUD вопросов отдельного опроса  **polls/[id опроса]/questions/**

_Пример : http://127.0.0.1:8000/api/polls/1/questions/_

CRUD отдельного вопроса **polls/[id опроса]/questions/[id вопроса]**

_Пример : http://127.0.0.1:8000/api/polls/1/questions/1/_

CRUD вариантов ответа на вопрос **polls/[id опроса]/questions/[id вопроса]/choices**

_Пример : http://127.0.0.1:8000/api/polls/1/questions/1/choices/_

CRUD вариантов ответа на вопрос **polls/[id опроса]/questions/[id вопроса]/choices/[id варианта]**

_Пример : http://127.0.0.1:8000/api/polls/1/questions/1/choices/1/_

CRUD ответов **polls/[id опроса]/questions/[id вопроса]/answers/**

_Пример : http://127.0.0.1:8000/api/polls/1/questions/1/answers/_

CRUD ответов **polls/[id опроса]/questions/[id вопроса]/answers/1/**

_Пример : http://127.0.0.1:8000/api/polls/1/questions/1/answers/1/_

CRUD пользователей **users/**

Просмотр пройденных опросов **users/[id пользователя]/completed_polls/**

_!(Фунция работает некорректно)_

_Пример : http://127.0.0.1:8000/api/users/1/completed_polls/_