web: gunicorn lryics_web.wsgi:application --log-file -
python manage.py collectstatic --noinput
manage.py migrate
