apt-get install python-module-django
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
docker compose up -d;
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver