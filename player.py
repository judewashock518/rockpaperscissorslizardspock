

class Player():
    def __init__(self, name):
        self.score = 0
        self.name = name

    def choose_gesture(self):
        while self.score < 3:
            gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

