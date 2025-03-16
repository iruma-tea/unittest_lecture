from unittest import TestCase

from janken.hands import rock, paper, scissors
from janken.player import CHOICES, Player


class TestPlayer(TestCase):
    """Player手のテスト(共通化しないパターン)"""

    def test_choice_rock(self):
        player = Player()
        player.hand = CHOICES['g']
        self.assertEqual(player.hand, rock)

    def test_choice_paper(self):
        player = Player()
        player.hand = CHOICES['p']
        self.assertEqual(player.hand, paper)

    def test_choice_scissors(self):
        player = Player()
        player.hand = CHOICES['c']
        self.assertEqual(player.hand, scissors)
