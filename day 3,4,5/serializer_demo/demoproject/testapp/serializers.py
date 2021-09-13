from rest_framework import serializers
from .models import Student

'''
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    address = serializers.CharField(max_length=100)
    marks = serializers.FloatField()

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.address = validated_data.get('address',instance.address)
        instance.marks = validated_data.get('marks',instance.marks)
        instance.save()
        return instance

'''

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'