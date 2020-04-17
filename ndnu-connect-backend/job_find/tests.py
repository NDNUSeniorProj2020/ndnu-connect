from django.test import TestCase
from rest_framework.test import APITestCase
from accounts.models import User
from .models import Job


class JobsTestCase(TestCase):
    def setUp(self):
        user1 = User.objects.create_user("JeffTest@gmail.com", "workerpassword")

        job1 = Job(title="testjob1", description="description test", company="Google", location="Mountain View, CA",
                      qualifications="bs degree", pay="1234", link="google.com", user=user1, type='FULL')
        job1.save()
        job2 = Job(title="testjob2", description="description test", company="Google", location="Mountain View, CA",
                      qualifications="bs degree", pay="1234", link="google.com", user=user1, type='FULL')
        job2.save()

    def testJobTitle(self):
        job1 = Job.objects.get(pk=1)
        job2 = Job.objects.get(pk=2)

        self.assertEqual(job1.title, 'testjob1')
        self.assertEqual(job2.title, 'testjob2')

    def testJobToString(self):
        job1 = Job.objects.get(pk=1)
        job2 = Job.objects.get(pk=2)

        self.assertEqual(str(job1), "Job Posting: testjob1")
        self.assertEqual(str(job2), "Job Posting: testjob2")
        
