для сборки проекта:<br>
установить docker<br>
Создать .env и прописывать в него переменные среды по образцу из env_example<br>
запустить проект:<br>
docker-compose up -d --build


Наполняем базу из dump.json:<br>
docker exec -it hw_drf-app-1 python manage.py loaddata dump.json 


пользователи:<br>
first_admin@sky.pro,<br>
moder1@sky.pro - состоит в группе moderators<br>
user1@sky.pro, user2@sky.pro<br>
пароль у всех 1qaz2wsx
