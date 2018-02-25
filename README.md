# wlc-django-rewrite
A Django version of the West London Coders website.

Make sure your version of python is 3.0 or higher. If you have several versions of python, use pyenv. You can use ```python3```
instead of ```python``` if that doesn't work for you, and use virtualenv instead of pyenv. Unfortunately pyenv is a massive
pain to get working for beginners. 

Clone the repo and run ``` python manage.py migrate ``` to create the DB.

Run ``` python manage.py runserver ``` to run the server. Go to 'http://127.0.0.1:8000/main/'. They'll be a 'Hello'.
