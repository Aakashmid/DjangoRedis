from django.db import connection
from django.http import HttpRequest, HttpResponse
from CacheApp.models import Product
from django.core.cache import cache
from django.forms.models import model_to_dict
import re

class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request: HttpRequest):        
        response = self.get_response(request)

        sample_model_table = Product._meta.db_table
        deleted_id=[]
        for query in connection.queries :
            if sample_model_table in query['sql']:
                sql=query['sql'].lower()
                if 'delete from' in sql:
                    # Extract ID from DELETE query
                    id_match = re.search(r'where\s+.*?"CacheApp_product"\."id"\s*in\s*\((\d+)\)', sql, re.IGNORECASE)
                    if id_match:
                        deleted_id.append(id_match.group(1))
                    


        with connection.cursor() as cursor:
            cursor.execute(
        "SELECT id FROM {} WHERE updated_at > datetime('now', '-1 minute')".format(sample_model_table)
        )
            change_data_ids=cursor.fetchall()


        change_data_ids=[item[0] for item in change_data_ids]
        print(f'changed ids {change_data_ids}')
        # change_data_ids=[item ]
        # print(f'deleted ids {deleted_id}')

        # updating cache 
        cache_data=cache.get('sample_data')
        if cache_data is not None:
            for id in change_data_ids:
                for index,item in enumerate(cache_data):
                    if item['id'] == id:
                        # cache_data[index]=model_to_dict(Product.objects.get(id=id))
                        pass
                cache.set('sample_data',cache_data)
        else:
            print("no cache data")
        return response 

  


