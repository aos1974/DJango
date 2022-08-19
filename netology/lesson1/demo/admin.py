from django.contrib import admin
from demo.models import Car, Person, Product, Order, OrderPosition

# Register your models here.

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = 'id', 'brand', 'model', 'color'
    list_filter = ['brand']

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'car',

# урок Django.ORM2
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'price', 'category'#, 'orders', 'positions'
    list_filter = ['category']

class OrderPositionsInline(admin.TabularInline):
    model = OrderPosition
    extra = 3

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id']#, 'products', 'positions'
    inlines = [OrderPositionsInline,]

@admin.register(OrderPosition)
class OrderPositionsAdmin(admin.ModelAdmin):
    list_display = 'product', 'order', 'quantity'

