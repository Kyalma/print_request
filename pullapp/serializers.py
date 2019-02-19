from rest_framework import serializers
from pullapp.models import SubmissionModel
from pullapp.models import ConsumableModel
from pullapp.models import PrinterModel
from pullapp.models import SlicerParamsModel


class SubmissionCreateOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmissionModel
        fields = ('designation', 'about', 'stl', 'material', 'copies')


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmissionModel
        fields = ('designation', 'about', 'stl', 'material', 'copies')
        read_only_fields = ('stl', )


class SubmissionListAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmissionModel
        fields = '__all__'


class ConsumableCreateOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsumableModel
        fields = ('consumable', 'variant', 'diameter', 'available')


class ConsumableSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsumableModel
        fields = ('consumable', 'variant', 'diameter', 'available')
        read_only_fields = ('consumable', 'variant', 'diameter')


class ConsumableListAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsumableModel
        fields = '__all__'


class PrinterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrinterModel
        fields = ('name', 'brand_model', 'layer_precision', 'hotend_size',
                  'x_size', 'y_size', 'z_size', 'dual_extruder', 'heated_bed')


class PrinterListAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrinterModel
        fields = '__all__'


class SlicerParamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlicerParamsModel
        fields = ('printer', 'hotend_diameter', 'layer_resolution', 'support')


class SlicerParamsListAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlicerParamsModel
        fields = '__all__'
