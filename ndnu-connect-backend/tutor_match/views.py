from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import UpdateAPIView, RetrieveAPIView
from rest_framework.response import Response

from .models import Department, Subject, Schedule, Tutor, Student
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


# Tutor API Views
class TutorViewSet(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer


class TutorUpdateView(UpdateAPIView):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer


class TutorRetrieveView(RetrieveAPIView):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer

    @api_view(['GET'])
    def tutor_details(request, pk):
        tutor = Tutor.objects.get(id=pk)
        serializer = TutorSerializer(tutor)
        return Response(serializer.data)


# Student API Views
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentUpdateView(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRetrieveView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    @api_view(['GET'])
    def student_details(request, pk):
        student = Student.objects.get(id=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
