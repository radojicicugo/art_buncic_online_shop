from rest_framework import serializers
from . models import BackendArt

class BackendArtSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackendArt
        fields = '__all__'
