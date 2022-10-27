from human import Human
from ai import AI
from player import Player
import random


class Game():
    def __init__(self):
        self.player1 = None
        self.player2 = None
        self.goes_first = self.player1

    def run_game(self):
        self.display_welcome()
        self.choose_player()
        self.current_turn()
        self.compare_gestures()
        self.display_winner()
        self.display_farewell()

    def display_welcome(self):
        print('Rock, Paper, Scissors, Lizard, Spock: Best Of Three!')
        print()
        print('Rules of the game:')
        print()
        print('Scissors cuts Paper')
        print('Paper covers Rock')
        print('Rock crushes Lizard')
        print('Lizard poisons Spock')
        print('Spock smashes Scissors')
        print('Scissors decapitaties Lizard')
        print('Lizard eats Paper')
        print('Paper disproves Spock')
        print('Spock vaporizes Rock')
        print('Rock crushes Scissors')
        print()

    def choose_player(self):
        answer = input("How many players")
        if answer == "1":
            self.player1 = Human("Steve")
            self.player2 = AI("Bot")
        elif answer == "2":
            self.player1 = Human("Steve")
            self.player2 = Human("Jude")
        else:
            self.player1 = AI("Bot")
            self.player2 = AI("Wilbur")

    def current_turn(self):
        while self.player1.score < 2 and self.player2.score < 2:
                self.player1.choose_gesture()
                self.player2.choose_gesture()
                if self.player1.chosen_gesture == self.player2.chosen_gesture:
                    print("It's a tie! Both players picked the same gesture. Keep playing.")
                    return self.player1.choose_gesture()
                elif self.player1.chosen_gesture == "Rock" and (self.player2.chosen_gesture == "Scissors" or self.player2.chosen_gesture == "Lizard"):
                    print(f'{self.player1.name} has won this round!')
                    self.player1.score += 1
                elif self.player1.chosen_gesture == "Paper" and (self.player2.chosen_gesture == "Rock" or self.player2.chosen_gesture == "Spock"):
                    print(f'{self.player1.name} has won this round!')
                    self.player1.score += 1
                elif self.player1.chosen_gesture == "Scissors" and (self.player2.chosen_gesture == "Lizard" or self.player2.chosen_gesture == "Paper"):
                    print(f'{self.player1.name} has won this round!')
                    self.player1.score += 1
                elif self.player1.chosen_gesture == "Lizard" and (self.player2.chosen_gesture == "Spock" or self.player2.chosen_gesture == "Paper"):
                    print(f'{self.player1.name} has won this round!')
                    self.player1.score += 1
                elif self.player1.chosen_gesture == "Spock" and (self.player2.chosen_gesture == "Scissors" or self.player2.chosen_gesture == "Rock"):
                    print(f'{self.player1.name} has won this round!')
                    self.player1.score += 1
            
            # elif self.goes_first == "PLAYER TWO" or self.goes_first == "AI":
            #     self.player2.choose_gesture()
            #     self.player1.choose_gesture()
            #     if self.player1.chosen_gesture == self.player2.chosen_gesture:
            #         print("It's a tie! Both players picked the same gesture. Keep playing.")
            #         return self.player2.choose_gesture()
            #     elif self.player1.chosen_gesture == "Rock" and (self.player2.chosen_gesture == "Scissors" or self.player2.chosen_gesture == "Lizard"):
            #         print(f'{self.player1.name} has won this round!')
            #         self.player1.score += 1
            #     elif self.player1.chosen_gesture == "Paper" and (self.player2.chosen_gesture == "Rock" or self.player2.chosen_gesture == "Spock"):
            #         print(f'{self.player1.name} has won this round!')
            #         self.player1.score += 1
            #     elif self.player1.chosen_gesture == "Scissors" and (self.player2.chosen_gesture == "Lizard" or self.player2.chosen_gesture == "Paper"):
            #         print(f'{self.player1.name} has won this round!')
            #         self.player1.score += 1
            #     elif self.player1.chosen_gesture == "Lizard" and (self.player2.chosen_gesture == "Spock" or self.player2.chosen_gesture == "Paper"):
            #         print(f'{self.player1.name} has won this round!')
            #         self.player1.score += 1
            #     elif self.player1.chosen_gesture == "Spock" and (self.player2.chosen_gesture == "Scissors" or self.player2.chosen_gesture == "Rock"):
            #         print(f'{self.player1.name} has won this round!')
            #         self.player1.score += 1
    
    def compare_gestures(self):
        pass

    def display_winner(self):
        pass

    def display_farewell(self):
        pass
