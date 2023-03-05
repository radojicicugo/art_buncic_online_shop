from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from . models import BackendArt
from . serializer import BackendArtSerializer
from rest_framework import viewsets
from django.db.models import Avg, Sum, Min, Max, Count


class BackendArtView(viewsets.ModelViewSet):
    queryset = BackendArt.objects.all()
    serializer_class = BackendArtSerializer
   
