from django.shortcuts import render
from .models import Student
from .serializers import StuSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET','POST'])

def all_data(req):
    if req.method=='POST':
        serializer=StuSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    data1 = Student.objects.all()
    serializer = StuSerializer(data1, many=True)
    return Response(serializer.data)