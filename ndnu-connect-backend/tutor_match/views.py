from django.shortcuts import render
from .models import Department, Subject, Schedule, Tutor, Student
from rest_framework import viewsets
from .serializers import DepartmentSerializer, SubjectSerializer, ScheduleSerializer, \
    TutorSerializer, StudentSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

# class TuitionMethodSerializer(viewsets.ModelViewSet):
#     queryset = TuitionMethod.objects.all()
#     serializer_class = TuitionMethodSerializer
#
# class TuitionLocationSerializer(viewsets.ModelViewSet):
#     queryset = TuitionLocation.objects.all()
#     serializer_class = TuitionLocationSerializer


class TutorViewSet(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
