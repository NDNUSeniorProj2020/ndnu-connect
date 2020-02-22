from django.test import TestCase

from accounts.models import person
from .models import Department, Subject, Schedule, Student, Tutor
from .serializers import DepartmentSerializer, SubjectSerializer, ScheduleSerializer, \
    StudentSerializer, TutorSerializer


class DepartmentTests(TestCase):
    def setUp(self):
        self.department_attributes = {
            'name': 'BUS',
        }

        self.serializer_data = {
            'name': 'ACC',
        }

        self.department = Department.objects.create(**self.department_attributes)
        self.serializer = DepartmentSerializer(instance=self.department)

    def test_contains_expected_fields(self):
        data = self.serializer.data

        self.assertCountEqual(data.keys(), ['name'])

    def test_name_field_content(self):
        data = self.serializer.data

        self.assertEqual(data['name'], self.department_attributes['name'])

    def test_name_in_choices(self):
        self.department_attributes['name'] = 'OTP'

        serializer = DepartmentSerializer(instance=self.department, data=self.department_attributes)

        self.assertFalse(serializer.is_valid())
        self.assertCountEqual(serializer.errors.keys(), ['name'])


class SubjectTests(TestCase):
    def setUp(self):
        self.subject_attributes = {
            'subject': 'Math',
            'semester': 'Spring 2020',
            'course_number': '2886',
        }

        self.serializer_data = {
            'subject': 'Computer Science',
            'semester': 'Spring 2019',
            'course_number': '2230',
        }

        self.subject = Subject.objects.create(**self.subject_attributes)
        self.serializer = SubjectSerializer(instance=self.subject)

    def test_contains_expected_fields(self):
        data = self.serializer.data

        self.assertCountEqual(data.keys(), ['subject', 'semester', 'course_number'])

    def test_field_contents(self):
        data = self.serializer.data

        self.assertEqual(data['subject'], self.subject_attributes['subject'])
        self.assertEqual(data['semester'], self.subject_attributes['semester'])
        self.assertEqual(data['course_number'], self.subject_attributes['course_number'])


class ScheduleTests(TestCase):
    def setUp(self):
        self.schedule_attributes = {
            'monday': '8AM-3PM',
            'tuesday': '7AM-2PM',
            'wednesday': '6AM-1PM',
            'thursday': '9AM-4PM',
            'friday': '10AM-5PM',
            'saturday': '11AM-6PM',
            'sunday': '12PM-7PM'
        }

        self.serializer_data = {
            'monday': '2AM-11PM',
            'tuesday': '3AM-9PM',
            'wednesday': '4AM-3PM',
            'thursday': '5AM-6PM',
            'friday': '6AM-2PM',
            'saturday': '1AM-4PM',
            'sunday': '12AM-8PM'
        }

        self.schedule = Schedule.objects.create(**self.schedule_attributes)
        self.serializer = ScheduleSerializer(instance=self.schedule)

    def test_contains_expected_fields(self):
        data = self.serializer.data

        self.assertCountEqual(data.keys(), ['monday', 'tuesday', 'wednesday',
                                            'thursday', 'friday', 'saturday', 'sunday'])

    def test_field_contents(self):
        data = self.serializer.data

        self.assertEqual(data['monday'], self.schedule_attributes['monday'])
        self.assertEqual(data['tuesday'], self.schedule_attributes['tuesday'])
        self.assertEqual(data['wednesday'], self.schedule_attributes['wednesday'])
        self.assertEqual(data['thursday'], self.schedule_attributes['thursday'])
        self.assertEqual(data['friday'], self.schedule_attributes['friday'])
        self.assertEqual(data['saturday'], self.schedule_attributes['saturday'])
        self.assertEqual(data['sunday'], self.schedule_attributes['sunday'])


class TutorTests(TestCase):
    pass
    # def setUp(self):
    #
    #     self.subject_for_tutor = {
    #         'subject': 'Math',
    #         'semester': 'Spring 2020',
    #         'course_number': '2886'
    #     }
    #
    #     self.subject = Subject.objects.create(**self.subject_for_tutor)
    #
    #     self.schedule_for_tutor = {
    #         'monday': '2AM-11PM',
    #         'tuesday': '3AM-9PM',
    #         'wednesday': '4AM-3PM',
    #         'thursday': '5AM-6PM',
    #         'friday': '6AM-2PM',
    #         'saturday': '1AM-4PM',
    #         'sunday': '12AM-8PM'
    #     }
    #
    #     self.schedule = Schedule.objects.create(**self.schedule_for_tutor)
    #
    #     self.person_for_tutor = {
    #         'person_name': 'Jimmy Franks',
    #         'email': 'jimmyfranks@aol.com'
    #     }
    #
    #     self.person = person.objects.create(**self.person_for_tutor)
    #
    #     self.tutor_attributes = {
    #         'pay': 20.02,
    #         'subject': self.subject,
    #         'credentials': 'BS Mathematics',
    #         'method': 2,
    #         'location': 2,
    #         'description': 'I teach math',
    #         'schedule': self.schedule,
    #         'rating': 4.2,
    #         'num_of_ratings': 123,
    #         'person': self.person
    #     }
    #
    #     self.tutor = Tutor.objects.create(**self.tutor_attributes)
    #     self.serializer = TutorSerializer(instance=self.tutor)
    #
    # def test_contains_expected_fields(self):
    #     data = self.serializer.data
    #
    #     self.assertCountEqual(data.keys(), ['pay', 'subject', 'credentials', 'method',
    #                                         'location', 'description', 'schedule',
    #                                         'rating', 'num_of_ratings', 'person'])


class StudentTests(TestCase):
    pass


class PersonTests(TestCase):
    pass
