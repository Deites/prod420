from rest_framework import viewsets

from .serializers import DataFromHubSerializer

from datahub.models import DataFromHub


class DataFromHubViewsets(viewsets.ModelViewSet):
    serializer_class = DataFromHubSerializer
    queryset = DataFromHub.objects.all()

    

