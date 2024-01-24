from django.shortcuts import render, redirect
import json
from .models import Doc

def index(request):
    return render(request, 'index.html')

def option_link(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    return render(request, 'index.html')

def option_upload(request):
    if request.method == 'POST':
        print(request.FILES)
        doc = Doc(docfile=request.FILES['file'])
        doc.save()
        return redirect('index')
    return render(request, 'index.html')

