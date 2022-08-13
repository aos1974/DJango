from datetime import datetime
import random
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator

from demo.models import Car, Person, Order, Product, OrderPosition

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

def create_car(request):
    car = Car(
        brand=random.choice(['Ferrari', 'McLaren', 'Bugatti', 'BMW', 'Lambo', 'Pagany']), 
        model=random.choice(['F1', 'P1', 'B1', 'A1', 'F22', 'B13', 'P2', 'A16']), 
        color=random.choice(['Red', 'Yellow', 'Black', 'White', 'Silver', 'Green', 'White fog']),
        )
    car.save()
    return HttpResponse(f'Car was created! {car.brand} {car.model}')

def list_car(request):
    brand = request.GET.get('brand', '')
    model = request.GET.get('model', '')
    color = request.GET.get('color', '')
    car_obj = Car.objects.filter(brand__contains=brand, model__contains=model, color__contains=color)
    cars = [f'{car.brand} {car.model} : {car.color} | {car.owners.count()}' for car in car_obj]
    return HttpResponse('<br>'.join(cars))

def create_person(request):
    cars = Car.objects.all()
    for car in cars:
        Person(name=random.choice(['Piter', 'Swong', 'Kim', 'Vasiay', 'Lana', 'Brooklin', 'Momondo', 'Paul']), car=car).save()
    return HttpResponse('All owners created sacsessfull!')

def list_person(request):
    p_obj = Person.objects.all()
    persons = [f'name: {p.name} car: {p.car.brand}-{p.car.model} {p.car.color}' for p in p_obj]
    return HttpResponse('<br>'.join(persons))

##################################
# Django.ORM 2
##################################

def list_orders(request):
    template = 'orders.html'
    orders = Order.objects.all()
    #orders = Order.objects.filter(positions__product__price__gte=44),
    context = {
        'orders': orders,
    } 
    return render(request, template, context)