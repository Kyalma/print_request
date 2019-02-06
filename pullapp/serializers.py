from rest_framework import serializers
from pullapp.models import SubmissionModel


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmissionModel
        fields = ('designation', 'about', 'stl', 'material', 'copies')
