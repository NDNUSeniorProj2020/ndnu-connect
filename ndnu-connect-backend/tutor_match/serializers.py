from rest_framework import serializers
from tutor_match.models import Department,Subject,Schedule,TuitionMethod,TuitionLocation,Tutor,Student
from rest_framework.viewsets import ModelViewSet

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ['name']

class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = ['subject','semester','course_number']


class ScheduleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Schedule
        fields = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']


# class TuitionMethodSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = TuitionMethod
#         fields = []
#
# class TuitionLocationSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = TuitionLocation
#         fields = []

class TutorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tutor
        fields = ['pay','subject','credentials','method','location','description','schedule']


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['YearInSchool','major','pay','standing','method','location','description','schedule']