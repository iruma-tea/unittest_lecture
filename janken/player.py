from abc import ABC
from janken.hands import rock, scissors, paper

# プレイヤーの選択肢
CHOICES = {
    'g': rock,
    'c': scissors,
    'p': paper
}


class Player(ABC):
    """プレイヤーの基底クラス"""

    def __init__(self):
        self.hand = None

    def choice_hand(self):
        """プレイヤーが選択するための抽象メソッド"""
        pass
