from django.shortcuts import render
from .models import Student
from .serializers import StuSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import Http404
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


@api_view(['GET','PUT','PATCH','DELETE'])
def data(req,pk):
    data=Student.objects.filter(id=pk)
    if data:
        if req.method=='PUT':
            snippet = Student.objects.get(pk=pk)
            serializer = StuSerializer(snippet, data=req.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif req.method=='PATCH':
            snippet = Student.objects.get(pk=pk)
            serializer = StuSerializer(snippet, data=req.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif req.method=='DELETE':
            snippet = Student.objects.get(pk=pk)
            snippet.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif req.method=='GET':
            snippet = Student.objects.get(pk=pk)
            serializer = StuSerializer(snippet)
            return Response(serializer.data)
    data={"msg":"Id is not present in DB"}
    return Response(data)
    
