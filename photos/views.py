from django.shortcuts import render

# Create your views here.
def welcome(requst):
    return HttpResponse ('Welcome to photo Gallery')
