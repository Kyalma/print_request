from django.shortcuts import render

from rest_framework import mixins, generics

from pullapp.serializers import SubmissionSerializer
from pullapp.models import SubmissionModel


class SubmissionListGenericAPI(mixins.ListModelMixin,
                               generics.GenericAPIView):
    serializer_class = SubmissionSerializer
    queryset = SubmissionModel.objects.all()

    def get(self, request, *args, **kwargs):
        """
        Get the list of all submissions
        """
        return self.list(request, *args, **kwargs)


class SubmissionPostGenericAPI(mixins.CreateModelMixin,
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
                           generics.GenericAPIView):
    serializer_class = SubmissionSerializer
    queryset = SubmissionModel.objects.all()

    def get(self, request, *args, **kwargs):
        """
        Retreive a submission
        """
        return self.retreive(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """
        Update a submission
        """
        return self.partial_update(request, *args, **kwargs)


class UserSubmissionListGenericAPI(mixins.ListModelMixin,
                                   generics.GenericAPIView):
    serializer_class = SubmissionSerializer
    queryset = SubmissionModel.objects.all()  # NO

    def get(self, request, *args, **kwargs):
        """
        List all submission from a user
        """
        return self.list(request, *args, **kwargs)
