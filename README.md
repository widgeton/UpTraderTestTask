# Запуск и тестирование
Чтобы создать локальную тестовую базу данных **SQLite**, в директории проекта нужно запустить команду
`python manage.py migrate`. Для заполнения тестовыми данными была создана команда, которая создает 3 меню с
3 категориями в каждом и подкатегориями с 4 уровнями вложенности. Чтобы заполнить базу, нужно запустить команду
`python manage.py create_test_models`. После этого перейти по адресу `127.0.0.1:8000/menus/` и проверить работу.
Для взаимодействия с базой через административную панель необходимо после миграции создать суперпользователя командой
`python manage.py createsuperuser`, перейти по адресу `127.0.0.1:8000/admin/` и ввести данные созданного пользователя.