from django.shortcuts import render,HttpResponse
from django.core.cache import cache
from .models import Product
# Create your views here.

def home(request):
    data = cache.get('sample_data')

    if not data:
        data = list(Product.objects.all().values())
        cache.set('sample_data', data, timeout=60*1) 
    return render(request, 'CacheApp/index.html', {'data': data})