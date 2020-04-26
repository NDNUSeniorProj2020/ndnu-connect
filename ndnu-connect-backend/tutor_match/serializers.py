from rest_framework import serializers

from .models import Department, Subject, Schedule, Tutor, Student
from generic_relations.relations import GenericRelatedField


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
    subject = SubjectSerializer(many=True, read_only=True)

    class Meta:
        model = Tutor
        fields = ['pay', 'subject', 'credentials', 'method',
                  'location', 'description', 'schedule',
                  'rating', 'num_of_ratings', 'user']


class StudentSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ['major', 'pay', 'standing', 'method', 'subject',
                  'location', 'description', 'schedule', 'user']

        subject = GenericRelatedField({
            Subject: SubjectSerializer(),
        })

        class Meta:
            model = Subject
            fields = ('subject', 'semester', 'course_number')
