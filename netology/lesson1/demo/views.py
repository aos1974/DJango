from datetime import datetime
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    return HttpResponse('Hello Django!')

def get_time(request):
    return HttpResponse(f'Time now : {datetime.now().time()}')

def hello(request):
    template_name = 'demo.html'
    name = request.GET.get('name', 'Nutria')
    context = {
        'name': name,
    }
    return render(request, template_name, context)
    #return HttpResponse(f'Hello {name} form DJ.')

def sum(request, a, b):
    result = int(a) + int(b)
    return HttpResponse(f'Sum = {result}')

def echo_date(request, dt: datetime):
    return HttpResponse(f'ECHO date: {dt.date()}')

CONTENT = [chr(i)*3 for i in range(1000)]

def pagi(request):
    page = request.GET.get('page', '0')
    page = int(page)
    template_name = 'pagi.html'
    paginator = Paginator(CONTENT, 10)
    context = {
        'page': paginator.get_page(page),
    }
    return render(request, template_name, context)