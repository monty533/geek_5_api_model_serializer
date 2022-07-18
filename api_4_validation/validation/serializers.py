from wsgiref.validate import validator
from rest_framework import serializers
from .models import Student

# validators


def start_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('name should start with r')


class StudentSerializer(serializers.Serializer):
    # id = serializers.IntegerField()
    name = serializers.CharField(max_length=50, validators=[start_with_r])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=50)

    # for creating or inserting data into the database

    def create(self, validate_data):
        return Student.objects.create(**validate_data)

    def update(self, instance, validate_data):
        print(instance.name)
        instance.name = validate_data.get('name', instance.name)
        print(instance.name)
        instance.roll = validate_data.get('roll', instance.roll)
        instance.city = validate_data.get('city', instance.city)
        instance.save()
        return instance

    ''' Three types of validation 1 = filed level validation, 2 = object level validation '''
    # field level validation this is only for single field validation

    def validate_roll(self, value):  # this method call when the serializer.is_valid() call
        if value >= 200:
            raise serializers.ValidationError('seat full')
        return value

    # object level validation this is only for multiple field validation

    def validate(self, data):  # data is python dictionary of field values
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'nitin kumar' and ct.lower() != 'ranchi':
            raise serializers.ValidationError('city must be ranchi')
        return data
