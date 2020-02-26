from django.shortcuts import render
from .serializers import JobSerializer
from .models import Job
from rest_framework import viewsets

# Create your views here.

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
