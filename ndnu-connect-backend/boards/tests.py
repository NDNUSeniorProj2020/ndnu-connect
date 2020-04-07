from django.test import TestCase
from accounts.models import User
from .models import Board, Topic, Post


class BoardTestCase(TestCase):
    def setUp(self):
        user1 = User.objects.create_user("JeffTest@gmail.com", "workerpassword", "jeffworker")
        user2 = User.objects.create_user('JonTest@gmail.com', 'tutorpassword', 'jontutor')

        board1 = Board(name='Events', description='Upcoming events at NDNU')
        board1.save()
        board2 = Board(name='Textbooks', description='Buy or sell textbooks')
        board2.save()

        topic1 = Topic(subject='My Birthday', board=board1, starter=user1)
        topic1.save()
        topic2 = Topic(subject='Not My Birthday', board=board2, starter=user2)
        topic2.save()
        '''
        post1 = Post(name='Events', description='Upcoming events at NDNU')
        post1.save()
        post2 = Post(name='Textbooks', description='Buy or sell textbooks')
        post2.save()
        '''

    def testBoardNames(self):
        board1 = Board.objects.get(name="Events")
        board2 = Board.objects.get(name="Textbooks")
        self.assertEqual(board1.name, 'Events')
        self.assertEqual(board2.name, 'Textbooks')

    def testPostNames(self):
        topic1 = Topic.objects.get(subject="My Birthday")
        topic2 = Topic.objects.get(subject="Not My Birthday")
        self.assertEqual(topic1.subject, 'My Birthday')
        self.assertEqual(topic2.subject, 'Not My Birthday')

    '''
    def testPostNames(self):
        post1 = Post.objects.get(name="Events")
        post2 = Post.objects.get(name="Textbooks")
        self.assertEqual(post1.name, 'Events')
        self.assertEqual(post2.name, 'Textbooks')
    '''