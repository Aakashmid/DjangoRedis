from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from django.core.cache import cache
from .models import Product
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

def home(request):
    data = cache.get('sample_data')

    if not data:
        data = list(Product.objects.all().values())
        # print(data)
        cache.set('sample_data', data) 
    return render(request, 'CacheApp/index.html', {'data': data})

@csrf_exempt
def webhook_receiver(request):
    if request.method=="POST":
        data=json.loads(request.body)
        print(data)
        return  JsonResponse({'status':'success'})
    else :
        return  JsonResponse({'error':'Invalid request method !!'})
