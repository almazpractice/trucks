# reksoft_trucks
тестовое задание на вакансию мидл python разработчика

### Описание
![Задание](app/static/img/task.jpg?raw=true)


### Технологии
Python 3.7, Django 2.2

### Как запустить проект
- Клонировать репозиторий и перейти в него в командной строке.
```Bash
git clone git@github.com:almazpractice/reksoft_trucks.git

cd reksoft_trucks
```
- Создайте файл .env с содержимым:
```Bash
SECRET_KEY=d@t!z&i2_a+7z1gt&8j9
DEBUG=False
DEVELOPMENT=development
```

- - Создать и активировать виртуальное окружение:
```Bash
python -m venv env

source env/Scripts/activate

python -m pip install --upgrade pip
```
- Установить зависимости из файла requirements.txt:
```Bash
pip install -r requirements.txt
```
- Выполнить миграции:
```Bash
python manage.py migrate
```
- Запустить проект:
```Bash
$ python manage.py runserver
```


Разработчик:
- :white_check_mark: [almazpractice](https://github.com/almazpractice)
[![telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/a_gimaev)

