![example workflow](https://github.com/surdex/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

### Проект развёрнут на адресе http://84.201.130.43/

# Контейнеризация и развёртывание на сервере учебного проекта API сервиса YaMDb с помощью Docker.

Проект собирает отзывы пользователей о фильмах, книгах, музыке и др., которым можно присваивать жанр.

В это версии прописан скрипт для GitHub Actions, делающий автоматические тесты,
загрузку образа на DockerHub, на "боевой" сервер Яндекс.Облака и отправку
сообщения об успешном завершении этих действий через TelegramBot.

Используются Python 3.8.5, Django и DRF, JWT-токены для аутентификации.
Формат передачи данных API - JSON. У неаутентифицированных пользователей
доступ к API только на чтение.

## Развернуть проект в Docker:

Собрать и запустить контейнер:

```
docker-compose up -d
```

Выполнить миграции:

```
docker-compose exec web python manage.py migrate --noinput
```

Заполнить БД началными данными:

```
python manage.py loaddata fixtures.json
```

Создать суперпользователя:

```
docker-compose exec web python manage.py createsuperuser
```

Собрать статику:

```
docker-compose exec web python manage.py collectstatic
```

## Примеры API запросов:

### Получение JWT-токена в обмен на email и confirmation_code - http://127.0.0.1/api/v1/auth/token/

POST request:

```
{
  "email": "string",
  "confirmation_code": "string"
}
```

Response:

```
{
  "token": "string"
}
```


### Отправление confirmation_code на переданный email - http://127.0.0.1/api/v1/auth/email/

POST request:

```
{
  "email": "string"
}
```

Response:

```
{
  "email": "string"
}
```


### Получить список всех отзывов/Создать новый - http://127.0.0.1/api/v1/titles/{title_id}/reviews/

GET Response:

```
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "id": 0,
        "text": "string",
        "author": "string",
        "score": 1,
        "pub_date": "2019-08-24T14:15:22Z"
      }
    ]
  }
]
```

POST Request:

```
{
  "text": "string",
  "score": 1
}
```

POST Response:

```
{
  "id": 0,
  "text": "string",
  "author": "string",
  "score": 1,
  "pub_date": "2019-08-24T14:15:22Z"
}
```


### Получить/обновить/удалить отзыв по id http://127.0.0.1/api/v1/titles/{title_id}/reviews/{review_id}/

PATCH Request:

```
{
  "text": "string",
  "score": 1
}
```

GET/PUT Response:

```
{
  "id": 0,
  "text": "string",
  "author": "string",
  "score": 1,
  "pub_date": "2019-08-24T14:15:22Z"
}
```

### Комментарии к отзывам

GET/PUT - http://127.0.0.1/api/v1/titles/{title_id}/reviews/{review_id}/comments/

GET Response:

```
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "id": 0,
        "text": "string",
        "author": "string",
        "pub_date": "2019-08-24T14:15:22Z"
      }
    ]
  }
]
```

POST Request:

```
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "id": 0,
        "text": "string",
        "author": "string",
        "pub_date": "2019-08-24T14:15:22Z"
      }
    ]
  }
]
```

POST Response:

```
{
  "id": 0,
  "text": "string",
  "author": "string",
  "pub_date": "2019-08-24T14:15:22Z"
}
```

По id комментария GET/PATCH/DELETE -
http://127.0.0.1/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/

PATCH Request:

```
{
  "text": "string"
}
```

Response:

```
{
  "id": 0,
  "text": "string",
  "author": "string",
  "pub_date": "2019-08-24T14:15:22Z"
}
```
