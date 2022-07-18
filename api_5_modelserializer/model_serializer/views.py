from django.shortcuts import render
import io
import json
from rest_framework.parsers import JSONParser
from .models import Student
from rest_framework.renderers import JSONRenderer
from .serializers import StudentSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

# Create your views here.

# class based crud application


@method_decorator(csrf_exempt, name='dispatch')
class student_api(View):  # sourcery skip: avoid-builtin-shadow
    def get(self, request, *args, **kwargs):  # sourcery skip: avoid-builtin-shadow
        json_data = request.body
        # print(json_data)
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        # print(type(pythondata))
        id = pythondata.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

        stu = Student.objects.all()
        # print(stu[0])
        serializer = StudentSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):  # sourcery skip: avoid-builtin-shadow
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(
            data=pythondata)  # variable name can by any
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data created'}
            # json_data = json.dumps(res)
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    def put(self, request, *args, **kwargs):  # sourcery skip: avoid-builtin-shadow
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=pythondata, partial=True)
        # complete update
        # serializer = StudentSerializer(stu, data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'data updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')

        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    def delete(self, request, *args, **kwargs):  # sourcery skip: avoid-builtin-shadow
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg': 'data deleted'}
        # json_data = JSONRenderer().render(res)
        # return HttpResponse(json_data, content_type='application/json')
        return JsonResponse(res, safe=False)
