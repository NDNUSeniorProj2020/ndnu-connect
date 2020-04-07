from django.test import TestCase
from .models import Board, Topic, Post


class BoardTestCase(TestCase):
    def setUp(self):
        board1 = Board(name='Events', description='Upcoming events at NDNU')
        board1.save()
        board2 = Board(name='Textbooks', description='Buy or sell textbooks')
        board2.save()

    def testBoardNames(self):
        board1 = Board.objects.get(name="Events")
        board2 = Board.objects.get(name="Textbooks")
        self.assertEqual(board1.name, 'Events')
        self.assertEqual(board2.name, 'Textbooks')
