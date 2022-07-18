from rest_framework import serializers
from .models import Student

# in this model serializer we don't have to make create and update method. In this those are in-built


class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True)
    def start_with_r(value):  # sourcery skip: instance-method-first-arg-name
        if value[0].lower() != 'r':
            raise serializers.ValidationError('name should start with r')
    name = serializers.CharField(validators=[start_with_r])

    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']
        # read_only_fields = ['name', 'roll']  # core arguements
        # extra_kwargs = {'name': {'read_only': True}}

    # validation
    # single level validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat full')
        return value

    # multi level validation
    def validate(self, data):  # data is python dictionary of field values
        print('naam', data)
        name = data.get('name')
        city = data.get('city')
        if name.lower() == 'nitin kumar' and city.lower() != 'ranchi':
            raise serializers.ValidationError('city must be ranchi')
        return data
