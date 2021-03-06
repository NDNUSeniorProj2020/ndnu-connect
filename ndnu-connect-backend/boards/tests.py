from django.test import TestCase
from accounts.models import User
from .models import Board, Topic, Post


class BoardTestCase(TestCase):
    def setUp(self):
        user1 = User.objects.create_user("JeffTest@gmail.com", "workerpassword")
        user2 = User.objects.create_user("JonTest@gmail.com", "tutorpassword")

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

    def testBoardToString(self):
        board1 = Board.objects.get(pk=1)
        board2 = Board.objects.get(pk=2)

        self.assertEqual(str(board1), 'Events')
        self.assertEqual(str(board2), 'Textbooks')

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

    def testTopicStarters(self):
        user1 = User.objects.get(pk=1)
        user2 = User.objects.get(pk=2)

        topic1 = Topic.objects.get(pk=1)
        topic2 = Topic.objects.get(pk=2)

        self.assertEqual(topic1.starter, user1)
        self.assertEqual(topic2.starter, user2)

    def testTopicToString(self):
        topic1 = Topic.objects.get(pk=1)
        topic2 = Topic.objects.get(pk=2)

        self.assertEqual(str(topic1), "Events: My Birthday")
        self.assertEqual(str(topic2), "Textbooks: Not My Birthday")

    def testPostMessages(self):
        post1 = Post.objects.get(pk=1)
        post2 = Post.objects.get(pk=2)

        self.assertEqual(post1.message, 'Who cares')
        self.assertEqual(post2.message, 'Good')

    def testPostTopics(self):
        topic1 = Topic.objects.get(pk=1)
        topic2 = Topic.objects.get(pk=2)

        post1 = Post.objects.get(pk=1)
        post2 = Post.objects.get(pk=2)

        self.assertEqual(post1.topic, topic1)
        self.assertEqual(post2.topic, topic2)

    def testPostCreatedBy(self):
        user1 = User.objects.get(pk=1)
        user2 = User.objects.get(pk=2)

        post1 = Post.objects.get(pk=1)
        post2 = Post.objects.get(pk=2)

        self.assertEqual(post1.created_by, user2)
        self.assertEqual(post2.created_by, user1)

    def testPostToString(self):
        post1 = Post.objects.get(pk=1)
        post2 = Post.objects.get(pk=2)

        self.assertEqual(str(post1), "Post #1 for Topic 'My Birthday' by user JonTest@gmail.com")
        self.assertEqual(str(post2), "Post #2 for Topic 'Not My Birthday' by user JeffTest@gmail.com")
