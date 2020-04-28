from rest_framework import serializers

from .models import Department, Subject, Schedule, Tutor, Student


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['name']


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['subject', 'semester', 'course_number']


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['monday', 'tuesday', 'wednesday',
                  'thursday', 'friday', 'saturday', 'sunday']


class TutorSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source='user.email', read_only=True, allow_null=True)

    class Meta:
        model = Tutor
        fields = ['pay', 'subject', 'credentials', 'method',
                  'location', 'description', 'schedule',
                  'rating', 'num_of_ratings', 'user', 'email']


class StudentSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source='user.email', read_only=True, allow_null=True)

    class Meta:
        model = Student
        fields = ['major', 'pay', 'standing', 'method',
                  'location', 'description', 'schedule', 'user', 'email']
