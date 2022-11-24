# api_final
### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/morhond/api_final_yatube.git
```

```
cd yatube_api
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

## Endpoints проекта:
Получить публикации списком или добавить публикацию:
```
http://127.0.0.1:8000/api/v1/posts/  # GET / POST 
```
Получить, изменить, удалить выбранную по id публикацию:
```
http://127.0.0.1:8000/api/v1/posts/{id}/  # GET / PUT / PATCH / DELETE
```
-------------------
Получить список комментариев к выбранной по id публикации списком или добавить к ней комментарий:
```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/  # GET / POST
```
Получить выбранный по id комментарий к выбранной по id публикации либо изменить или удалить его:
```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/  # GET / PUT / PATCH / DELETE
```
-------------------
Получить группы списком: 
```
http://127.0.0.1:8000/api/v1/groups/  # GET
```
Получить выбранную по id группу:
```
http://127.0.0.1:8000/api/v1/groups/{id}/  # GET
```
-------------------
Посмотреть свои подписки списком и подписаться на других авторов:
```
http://127.0.0.1:8000/api/v1/follow/  # GET / POST
```
-------------------
Получение JWT-токена:
```
http://127.0.0.1:8000/api/v1/jwt/create/
```
Обновление JWT-токена:
```
http://127.0.0.1:8000/api/v1/jwt/refresh/
```
Проверка JWT-токена:
```
http://127.0.0.1:8000/api/v1/jwt/verify/
```
## Доступ
Аутентифицированным пользователям разрешено изменение и удаление своего контента; 
в остальных случаях доступ предоставляется только для чтения.
Исключение — endpoint /follow/: доступ к нему есть только у аутентифицированных пользователей.
## Примеры
Получение списка публикаций: GET-запрос на endpoint http://127.0.0.1:8000/api/v1/posts/
```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```
Создание публикации: POST-запрос на endpoint http://127.0.0.1:8000/api/v1/posts/
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
* Публикация успешно создана (код 201):
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```
* Предоставлены неправильные данные (код 400):
```
{
  "text": [
    "Обязательное поле."
  ]
}
```