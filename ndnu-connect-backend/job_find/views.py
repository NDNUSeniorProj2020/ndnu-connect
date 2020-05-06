from .serializers import JobSerializer
from .models import Job
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.generics import UpdateAPIView, RetrieveAPIView


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobUpdateView(UpdateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobRetrieveView(RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    @api_view(["GET"])
    def job_details(request, pk):
        job = Job.objects.get(id=pk)
        serializer = JobSerializer(job)
        return Response(serializer.data)
