from rest_framework import serializers
from pullapp.models import SubmissionModel
from pullapp.models import ConsumableModel


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmissionModel
        fields = ('designation', 'about', 'stl', 'material', 'copies')


class ConsumableSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsumableModel
        fields = ('consumable', 'variant', 'diameter', 'available')
