from rest_framework import serializers, status
from rest_framework.response import Response

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


class SubjectPrimaryKeyRelatedField(serializers.RelatedField):

    def to_representation(self, value):
        return value.subject

    def to_internal_value(self, data):
        subject_id = data['id']
        return Subject.objects.get(id=subject_id)


class TutorSerializer(serializers.ModelSerializer):
    # def __init__(self, *args, **kwargs):
    #     subject = kwargs.pop('subject', True)
    #     super(TutorSerializer, self).__init__(many=subject, *args, **kwargs)

    email = serializers.CharField(source='user.email', read_only=True, allow_null=True)

    #  works to associate existing subject models to tutor, but cant view subjects as subjects as string
    # subject = SubjectPrimaryKeyRelatedField(many=True, queryset=Subject.objects.all())
    #subject = serializers.PrimaryKeyRelatedField(many=True, queryset=Subject.objects.all(), default=SubjectSerializer())
    subject = SubjectSerializer(many=True)

    def create(self, validated_data):
        subject = validated_data.pop('subject')

        serializer = self.get_serializer(data=validated_data.pop('subject'))
        serializer.is_valid(raise_exception=True)
        serializer.save(subject=subject)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        # subject_data = validated_data.pop('subject')
        # tutor = Tutor.objects.create(**validated_data)
        #
        # for subject in subject_data:
        #     Subject.objects.create(subject=subject, **subject)
        #
        # return tutor

    class Meta:
        model = Tutor
        fields = ['pay', 'subject', 'credentials', 'method',
                  'location', 'description', 'schedule',
                  'rating', 'num_of_ratings', 'user', 'email']

        subject = GenericRelatedField({
            Subject: SubjectSerializer(),
        })

        class Meta:
            model = Subject
            fields = ('subject', 'semester', 'course_number')


class StudentSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source='user.email', read_only=True, allow_null=True)

    subject = SubjectSerializer(many=True)

    class Meta:
        model = Student
        fields = ['major', 'pay', 'standing', 'method', 'subject',
                  'location', 'description', 'schedule', 'user', 'email']

        subject = GenericRelatedField({
            Subject: SubjectSerializer(),
        })

        class Meta:
            model = Subject
            fields = ('subject', 'semester', 'course_number')
