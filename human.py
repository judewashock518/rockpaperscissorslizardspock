from player import Player


class Human(Player):
    def __init__(self, name):
        super().__init__(name)


    def choose_gesture(self):
        for gesture in self.gesture_list:
            print(gesture)
        user_input = int(input("Select your move: 0-4: "))
        self.chosen_gesture = self.gesture_list[user_input]
        print(f"{self.name} has chosen {self.chosen_gesture}")