# My Blog

Тестовое приложение представляющее из себя блог, отображающее список постов из БД, созданное для ознакомления с Django Framework

## Quickstart

Run the following commands to bootstrap your environment:
    
    pip install virtualenv
    git clone https://github.com/niksergs/Django_Project_Blog
    cd my_blog

    python -m venv venv
    venv/Scripts/activate.bat
    pip install -r requirements/dev.txt

    cp .env.template .env

Run the app locally:

    python manage.py runserver 0.0.0.0:8000 --settings=my_site.settings.dev

Run the app with gunicorn:

    pip install gunicorn
    gunicorn my_site.wsgi:application -b 0.0.0.0:8000
    
