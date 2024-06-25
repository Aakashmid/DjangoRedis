from django.contrib import admin
from .models import Product
# Register your models here.
@admin.register(Product)
class product_admin(admin.ModelAdmin):
    list_display=['id','name','price']