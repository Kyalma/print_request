from django.shortcuts import render

from rest_framework import mixins, generics

from pullapp.serializers import SubmissionSerializer
from pullapp.serializers import ConsumableSerializer
from pullapp.serializers import PrinterSerializer
from pullapp.serializers import SlicerParamsSerializer
from pullapp.models import SubmissionModel
from pullapp.models import ConsumableModel
from pullapp.models import PrinterModel
from pullapp.models import SlicerParamsModel


class SubmissionListGenericAPI(mixins.ListModelMixin,
                               generics.GenericAPIView):
    serializer_class = SubmissionSerializer
    queryset = SubmissionModel.objects.all()

    def get(self, request, *args, **kwargs):
        """
        Get the list of all submissions
        """
        return self.list(request, *args, **kwargs)


class SubmissionCreateGenericAPI(mixins.CreateModelMixin,
                                 generics.GenericAPIView):
    serializer_class = SubmissionSerializer
    queryset = SubmissionModel.objects.all()

    def post(self, request, *args, **kwargs):
        """
        Create a submission
        """
        return self.create(request, *args, **kwargs)


class SubmissionGenericAPI(mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           generics.GenericAPIView):
    serializer_class = SubmissionSerializer
    queryset = SubmissionModel.objects.all()

    def get(self, request, *args, **kwargs):
        """
        Retreive a submission
        """
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """
        Update a submission
        """
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kargs):
        """
        Delete a submission
        """
        return self.destroy(request, *args, **kwargs)


class UserSubmissionListGenericAPI(mixins.ListModelMixin,
                                   generics.GenericAPIView):
    serializer_class = SubmissionSerializer
    queryset = SubmissionModel.objects.all()  # NO

    def get(self, request, *args, **kwargs):
        """
        List all submission from a user
        """
        return self.list(request, *args, **kwargs)


class ConsumableGenericAPI(mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           generics.GenericAPIView):
    serializer_class = ConsumableSerializer
    queryset = ConsumableModel.objects.all()

    def get(self, request, *args, **kwargs):
        """
        Retreive a consumable
        """
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """
        Update is a consumable is avaialble or not
        other fields should be read-only
        """
        # TODO
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kargs):
        """
        Delete a consumable
        """
        return self.destroy(request, *args, **kwargs)


class ConsumableCreateGenericAPI(mixins.CreateModelMixin,
                                 generics.GenericAPIView):
    serializer_class = ConsumableSerializer
    queryset = ConsumableModel.objects.all()

    def post(self, request, *args, **kwargs):
        """
        Retreive a consumable
        """
        return self.create(request, *args, **kwargs)


class ConsumableListGenericAPI(mixins.ListModelMixin,
                               generics.GenericAPIView):
    serializer_class = ConsumableSerializer
    queryset = ConsumableModel.objects.all()

    def get(self, request, *args, **kwargs):
        """
        List all the consumables
        """
        return self.list(request, *args, **kwargs)


class PrinterGenericAPI(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):
    serializer_class = PrinterSerializer
    lookup_field = 'id_printer'
    queryset = PrinterModel.objects.all()

    def get(self, request, *args, **kwargs):
        """
        Retreive a printer
        """
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """
        Update is a printer feature
        """
        # TODO
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        Delete a printer
        """
        return self.destroy(request, *args, **kwargs)


class PrinterCreateGenericAPI(mixins.CreateModelMixin,
                              generics.GenericAPIView):
    serializer_class = PrinterSerializer
    queryset = PrinterModel.objects.all()

    def post(self, request, *args, **kwargs):
        """
        Retreive a printer
        """
        return self.create(request, *args, **kwargs)


class PrinterListGenericAPI(mixins.ListModelMixin,
                            generics.GenericAPIView):
    serializer_class = PrinterSerializer
    queryset = PrinterModel.objects.all()

    def get(self, request, *args, **kwargs):
        """
        List all the printers
        """
        return self.list(request, *args, **kwargs)


class SlicerParamGenericAPI(mixins.CreateModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            generics.GenericAPIView):
    serializer_class = SlicerParamsSerializer
    queryset = SlicerParamsModel.objects.all()

    def get(self, request, *args, **kwargs):
        """
        Retrieve the current slicing params of a submission
        """
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Create slicing params for a submission
        Only one per submission can exist
        Return an error if there are existing params
        """
        return self.create(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """
        Update the slicing params of a submission
        """
        return self.partial_update(request, *args, **kwargs)
