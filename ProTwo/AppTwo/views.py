from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict = {'help' : 'I am your helper'}
    return render(request, 'AppTwo/help.html', context=my_dict)

def help(request):
    helpdict = {'help_insert' : 'HELP PAGE'}
    return render(request, 'AppTwo/help.html', context=helpdict)