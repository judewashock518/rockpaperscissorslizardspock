from player import Player
import random

class AI(Player):

    def __init__(self, name):
        super().__init__(name)


    def choose_gesture(self):
        self.chosen_gesture = self.gesture_list[random.randint(0,4)]
        print(f"{self.name} has chosen {gesture_list[int(self.chosen_gesture)]}")
        