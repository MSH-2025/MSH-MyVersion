source ./venv/bin/activate
docker compose up -d;
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
//python3 -m venv venv
//sudo apt-get install python-module-django
//pip install django==4.2.20
//pip install django-axes[ipware]
//pip install psycopg2-binary
//pip install django-auto-logout
//pip install django-debug-toolbar
//python -m pip install Pillow