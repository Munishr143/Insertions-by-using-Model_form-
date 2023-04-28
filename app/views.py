from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse

def insert_topic(request):
    TFO=Topic_Form()
    d={'TFO':TFO}

    if request.method=='POST':
        TFOD=Topic_Form(request.POST)

        if TFOD.is_valid():
            TFOD.save()
            return HttpResponse('Topic inserted Sucessfully')

    return render(request, 'insert_topic.html', d)

def insert_webpage(request):
    WFO=Webpage_Form()
    d={'WFO':WFO}

    if request.method=='POST':
        WFOD=Webpage_Form(request.POST)

        if WFOD.is_valid():
            WFOD.save()
            return HttpResponse('Webpage inserted Sucessfully')

    return render(request, 'insert_webpage.html', d)

def insert_AR(request):
    AFO=AccessRecord_Form()
    d={'AFO':AFO}

    if request.method=='POST':
        AFOD=AccessRecord_Form(request.POST)

        if AFOD.is_valid():
            AFOD.save()
            return HttpResponse('AccessRecord inserted Sucessfully')

    return render(request, 'insert_AR.html', d)

