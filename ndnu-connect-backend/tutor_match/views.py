from django.shortcuts import render
from tutor_match.models import Department,Subject,Schedule,TuitionMethod,TuitionLocation,Tutor,Student,SubjToDept
from rest_framework import viewsets
from tutor_match.serializers import DepartmentSerializer,SubjectSerializer,ScheduleSerializer, TutorSerializer,StudentSerializer
# Create your views here.
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class SubjectSerializer(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class ScheduleSerializer(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

# class TuitionMethodSerializer(viewsets.ModelViewSet):
#     queryset = TuitionMethod.objects.all()
#     serializer_class = TuitionMethodSerializer
#
# class TuitionLocationSerializer(viewsets.ModelViewSet):
#     queryset = TuitionLocation.objects.all()
#     serializer_class = TuitionLocationSerializer

class TutorSerializer(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer

class StudentSerializer(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer