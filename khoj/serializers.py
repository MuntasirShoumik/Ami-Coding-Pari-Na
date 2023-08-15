from rest_framework import serializers
from .models import InputRecord

class InputRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputRecord
        fields = ('timestamp', 'input_values')
