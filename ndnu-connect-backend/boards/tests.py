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

        post1 = Post(message='Who cares', topic=topic1, created_by=user2)
        post1.save()
        post2 = Post(message='Good', topic=topic2, created_by=user1)
        post2.save()

    def testBoardNames(self):
        board1 = Board.objects.get(pk=1)
        board2 = Board.objects.get(pk=2)
        self.assertEqual(board1.name, 'Events')
        self.assertEqual(board2.name, 'Textbooks')

    def testBoardDescriptions(self):
        board1 = Board.objects.get(pk=1)
        board2 = Board.objects.get(pk=2)
        self.assertEqual(board1.description, 'Upcoming events at NDNU')
        self.assertEqual(board2.description, 'Buy or sell textbooks')

    def testTopicSubjects(self):
        topic1 = Topic.objects.get(pk=1)
        topic2 = Topic.objects.get(pk=2)
        self.assertEqual(topic1.subject, 'My Birthday')
        self.assertEqual(topic2.subject, 'Not My Birthday')

    def testTopicBoards(self):
        board1 = Board.objects.get(pk=1)
        board2 = Board.objects.get(pk=2)
        topic1 = Topic.objects.get(pk=1)
        topic2 = Topic.objects.get(pk=2)
        self.assertEqual(topic1.board, board1)
        self.assertEqual(topic2.board, board2)
    """
    def testTopicStarters(self):
        topic1 = Topic.objects.get(pk=1)
        topic2 = Topic.objects.get(pk=2)
        self.assertEqual(topic1.starter, 'My Birthday')
        self.assertEqual(topic2.starter, 'Not My Birthday')
    """
    def testPostMessages(self):
        post1 = Post.objects.get(pk=1)
        post2 = Post.objects.get(pk=2)
        self.assertEqual(post1.message, 'Who cares')
        self.assertEqual(post2.message, 'Good')

    def testPostMessages(self):
        topic1 = Topic.objects.get(pk=1)
        topic2 = Topic.objects.get(pk=2)
        post1 = Post.objects.get(pk=1)
        post2 = Post.objects.get(pk=2)
        self.assertEqual(post1.topic, topic1)
        self.assertEqual(post2.topic, topic2)
