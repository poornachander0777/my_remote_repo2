from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def welcome(request):
    s='<h1>Hello Guys This is Poornachander Varukolu.. iam testing weather it is working or not?<br> And this is first django project.</h1>'
    p=datetime.datetime.now()
    p=f'<h1>{str(p)}</h1>'
    return HttpResponse(s)
