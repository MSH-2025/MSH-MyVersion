source ./venv/bin/activate
docker compose up -d;
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
