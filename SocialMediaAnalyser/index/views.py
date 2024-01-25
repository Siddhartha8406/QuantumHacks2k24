from django.shortcuts import render, redirect, HttpResponse
import json
from .models import Doc
from . import youtube
from .analyse_comment import CommentAnalyser
from django.conf import settings
import os

pos = []
neg = []
neu = []
file_url = ""

def index(request):
    return render(request, 'index.html')

def option_link(request):

    global body_unicode
    body_unicode = request.body.decode('utf-8')

    return HttpResponse(status=200)

def option_upload(request):
    global file_url
    if request.method == 'POST':
        doc = Doc(docfile=request.FILES['file'])
        doc.save()
        file_url = str(str(settings.BASE_DIR) + str(doc.docfile.url))
        return redirect('uploadResults')

def view_result(request):
    global body_unicode
    body = json.loads(body_unicode)

    video_id = body['link'].split('=')[1]
    commments = youtube.main(video_id)
    
    analyzer = CommentAnalyser()
    result = analyzer.analyze(commments)

    neg = result[0]
    neu = result[1]
    pos = result[2]

    return render(request, 'results.html', {'neg':neg, 'neu':neu, 'pos':pos})

def view_result_upload(requests):
    global file_url
    file = open(file_url, 'r')
    comments = file.read().split('\n')
    analyzer = CommentAnalyser()
    result = analyzer.analyze(comments)
    neg = result[0]
    neu = result[1]
    pos = result[2]

    print(neg, neu, pos)
    return render(request, 'results.html', {'neg':neg, 'neu':neu, 'pos':pos})

def uploadResults(request):
    pass
