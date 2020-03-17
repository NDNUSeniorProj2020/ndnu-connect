from .serializers import JobSerializer
from .models import Job
from rest_framework import viewsets


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
