from .serializers import JobSerializer
from .models import Job
from rest_framework import viewsets
from rest_framework.generics import UpdateAPIView



class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
class JobUpdateView(UpdateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
