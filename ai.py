from player import Player
import random

class AI(Player):

    def __init__(self, name):
        super().__init__()
        self.score = 0
        self.name = name

    def choose_gesture(self):
        self.chosen_gesture = str(random.randint(0,4))
        gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spoc"]
        print(f"{self.name} has chosen {gesture_list[int(self.chosen_gesture)]}")
        