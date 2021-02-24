###ACTIVAR ENT VIRTUAL
##crear proyecto 
python3 -m venv venv
./venv/Scripts/activate
pip install Django
pip freeze > requirements.txt
django-admin
django-admin startproject config .
python manage.py
python manage.py runserver
python manage.py migrate
python manage.py make migrations
python manage.py createsuperuser
django-admin startapp blog

###GLOSARIO###
