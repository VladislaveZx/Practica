import random

from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseNotFound

from . import models

class StudentsSerializator(serializers.ModelSerializer):
    class Meta:
        model = models.Students
        fields = ['studnum', 'studname', 'studgroup', 'studyear']


class StudentsInfo(APIView):
    def get(self, request, pk, format=None):
        student = models.Students.objects.get(studnum=pk)
        if not student:
            return HttpResponseNotFound()
        serialized_student = StudentsSerializator(student, many=False)
        
        return Response(serialized_student.data)


        
