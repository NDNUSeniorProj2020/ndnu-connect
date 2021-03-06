from django.test import TestCase
from .models import User


class AccountsTestCase(TestCase):
    def setUp(self):
        User.objects.create_user("JeffTest@gmail.com", "workerpassword")
        User.objects.create_user("JonTest@gmail.com", "tutorpassword")

    def testUserEmail(self):
        user1 = User.objects.get(pk=1)
        user2 = User.objects.get(pk=2)

        self.assertEqual(user1.email, 'JeffTest@gmail.com')
        self.assertEqual(user2.email, 'JonTest@gmail.com')

    def testUserToString(self):
        user1 = User.objects.get(pk=1)
        user2 = User.objects.get(pk=2)

        self.assertEqual(str(user1), 'JeffTest@gmail.com')
        self.assertEqual(str(user2), 'JonTest@gmail.com')
