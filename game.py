from random import random
from human import Human
from ai import AI
from player import Player


class Game():
    def __init__(self):
        self.player1 = None
        self.player2 = None

    def run_game(self):
        self.display_welcome()
        self.choose_player()
        self.play()
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

        self.goes_first = ''

    def play(self):
        first_turn = random.randint(1, 2)
        if first_turn == 1:
            print('PLAYER ONE goes first!')
            self.goes_first = "PLAYER ONE"
        if first_turn == 2:
            print('PLAYER TWO goes first!') or ('AI goes first!')
            self.goes_first = "PLAYER TWO" or "AI"

    def current_turn(self):
        while self.player1.score < 2 and self.player2.score < 2:
            if self.goes_first == "PLAYER ONE":
                self.player1.choose_gesture()
                self.player2.choose_gesture()
            elif self.goes_first == "PLAYER TWO" or self.goes_first == "AI":
                self.player2.choose_gesture()
                self.player1.choose_gesture()
    
    def compare_gestures(self):


    def display_winner(self):
        pass

    def display_farewell(self):
        pass
