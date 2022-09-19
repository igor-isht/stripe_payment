## Описание:

Тестовое задание: Django с одной страницей и несколькими методами API Stripe. 


Реализованы:
```
Docker

Environment variables

Django Admin панель  (явно не лучшим образом)

Модель Order

Модель Discount  (наверное не так, как представлял заказчик)
```

### Запуск:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/ln9var/stripe_payment.git
```

```
cd stripe_payment
```

Создать файл с переменными окружения .env:

```
touch shop/.env
```

При необходимости задать ключи окружения, (в настройках заданы  ключи по умолчанию):

```
DB_ENGINE=django.db.backends.postgresql

DB_NAME=postgres 

POSTGRES_USER=postgres

POSTGRES_PASSWORD=postgres

DB_HOST=db

DB_PORT=5432

SECRET_KEY='Your_secret_key' # Django

API_KEY='Your_secret_API_key'  # Stripe

DEBUG=True  (при желании)
```


Cоздать образ и контейнеры, сделать миграции, создать суперпользователя:

```

docker-compose up -d

docker-compose exec backend python manage.py migrate

docker-compose exec backend python manage.py collectstatic --no-input

docker-compose exec web python manage.py createsuperuser

```
Готово. Проект развернулся на [127.0.0.1](http://127.0.0.1) 


Теперь необходимо создать несколько товаров через панель администратора, и можно тестировать:

1) На страницах товаров (127.0.0.1/item/{pk}) есть кнопки "Добавить в корзину" и "Оформить заказ".

2) При нажатии "Добавить в корзину" создается объект Order, закрепленный за текущим пользователем, туда же добавляются другие товары

3) При нажатии "Оформить заказ" происходит перенаправление на 127.0.0.1/buy/{pk}, где pk - id пользователя. На нем происходит формирование запроса Session.create со списком покупок текущего пользователя и редирект на Checkout форму

Дополнительно можно реализовать удаление экземпляра Order после редиректа на страницу /success/
