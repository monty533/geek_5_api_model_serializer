from django.shortcuts import render
import io
import json
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serialize = StudentSerializer(data=pythondata)
        if serialize.is_valid():
            serialize.save()
            res = {'msg': 'Data created'}
            json_data = json.dumps(res)
            # json_data = JSONParser().parse(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serialize.errors)
        return HttpResponse(json_data, content_type='application/json')
