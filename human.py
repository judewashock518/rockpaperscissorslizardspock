from player import Player


class Human(Player):
    def __init__(self, name):
        super().__init__(name)


    def choose_gesture(self):
        index = 0
        for gesture in self.gesture_list:
            print(f'{index}) {gesture}')
            index += 1
        user_input = int(input("Select your gesture by choosing a number in chronological order from Rock to Spock, 0-4: "))
        if user_input in [0,1,2,3,4]:
            self.chosen_gesture = self.gesture_list[user_input]
            print(f"{self.name} has chosen {self.chosen_gesture}")
        else:
            print("Please choose a number/gesture between the values of 0 and 4")
            self.choose_gesture()

            #     if user_input != int(input(" 0-4")):
            # print("There are no further options for that number. Please try again.")
            # self.choose_gesture()