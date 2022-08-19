from django.http import HttpResponse
from django.shortcuts import render

from bboard.models import Bb

def index(request):
    s = 'Список объявлений \r\n\r\n'
    for bb in Bb.objects.order_by('-published'):
        s = s + bb.published.strftime("%m/%d/%Y, %H:%M:%S") + '\r\n' + bb.title + '\r\n' + bb.content + '\r\n\r\n'
    return HttpResponse(s, content_type='text/plain; charset=utf-8')
