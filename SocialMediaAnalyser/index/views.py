from django.shortcuts import render
import json

def index(request):
    return render(request, 'index.html')

def option_link(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    content = body['content']
    return render(request, 'inde.html')