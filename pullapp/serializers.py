from rest_framework import serializers
from pullapp.models import SubmissionModel
from pullapp.models import ConsumableModel
from pullapp.models import PrinterModel
from pullapp.models import SlicerParamsModel


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmissionModel
        fields = ('designation', 'about', 'stl', 'material', 'copies')
        read_only_fields = ('stl', )


class ConsumableSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsumableModel
        fields = ('consumable', 'variant', 'diameter', 'available')
        read_only_fields = ('consumable', 'variant', 'diameter')


class PrinterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrinterModel
        fields = ('name', 'brand_model', 'layer_precision', 'hotend_size',
                  'x_size', 'y_size', 'z_size', 'dual_extruder', 'heated_bed')


class SlicerParamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlicerParamsModel
        fields = ('printer', 'hotend_diameter', 'layer_resolution', 'support')
