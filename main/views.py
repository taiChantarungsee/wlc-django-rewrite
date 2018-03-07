from django.shortcuts import render
from django.http import HttpResponse

from .models import Member

def index(request):
	return response(request, 'index.html')

def members(request):
	#Return total members count and list of members.
	member_count = Member.objects.count()
	members = Member.objects.all() # reduce to one query by counting this?
	return response(request, 'members.html')

def hackrooms(request):
	return response(request, 'hackrooms.html')

#def hackroom?????

#def meetups(request):
	#All the API info is used here.
