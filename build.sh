set -o errexit

python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate
python manage.py migrate auth
