# Запуск

## Склонировать репозиторий

```bash
git clone https://github.com/CodyLikeSo/test_shop.git

# Затем
cd .\test_shop\
```

## Запустить docker-compose. Должен быть установлен на пк

```bash
docker-compose up --build -d
```

```bash
docker-compose exec web python manage.py migrate
```


```bash
docker-compose exec web python manage.py collectstatic --noinput 
```


```bash
docker-compose exec web python manage.py createsuperuser
# Далее создаем юзера
```

## Проходим на http://localhost:8000/admin и вводим те данные которые создали в команде выше(createsuperuser). Создаем категории и несколько товаров. Заходим на http://localhost:8000/ и проверяем. 

# Если что-то не работает - напишите мне в телеграм - t.me/demidovich_arseniy