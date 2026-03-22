from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'



# class StudentSerializer(serializers.ModelSerializer):
#     name = serializers.CharField(max_length=100,default='N/A')
#     email = serializers.EmailField(unique=True)
#     contact = serializers.CharField()
#     gender = serializers.CharField(max_length=10,default='N/A')
#     city = serializers.CharField(max_length=50,default='N/A')