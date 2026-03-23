from rest_framework import serializers
from .models import Student

class StuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

# class StudentSerializer(serializers.ModelSerializer):
#     name = serializers.CharField(max_length=100,default='N/A')
#     email = serializers.EmailField(unique=True)
#     contact = serializers.CharField()
#     gender = serializers.CharField(max_length=10,default='N/A')
#     city = serializers.CharField(max_length=50,default='N/A')

# class StudentSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     content = serializers.CharField(max_length=200)
#     created = serializers.DateTimeField()

#     def create(self, validated_data):
#         return Student(**validated_data)

#     def update(self, instance, validated_data):
#         instance.email = validated_data.get('email', instance.email)
#         instance.content = validated_data.get('content', instance.content)
#         instance.created = validated_data.get('created', instance.created)
#         instance.save()
#         return instance