from rest_framework import serializers

from datahub import models

class PlateNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PlateNumber
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Group
        fields = '__all__'

class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Direction
        fields = '__all__'

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Photo
        fields = '__all__'

class DataFromHubSerializer(serializers.ModelSerializer):
    plate_number = PlateNumberSerializer(required=False, many=True)
    group = GroupSerializer(required=False, many=True)
    direction = DirectionSerializer(required=False, many=True)
    photo = PhotoSerializer(required=False, many=True)

    class Meta:
        model = models.DataFromHub
        fields = '__all__'