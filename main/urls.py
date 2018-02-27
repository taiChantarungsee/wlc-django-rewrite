from django.urls import path

from views import *

urlpatterns = [
    path('', index, name='index'),
    path('/members/$', members, name='members'),
    path('/hackrooms/$', hackrooms, name='hackrooms'),
    path('/meetups/$', meetups, name='meetups'),
    path('/languages/$', languages, name='languages'),
    path('/posts/$', posts, name='posts'),
]