from random import random
from human import Human
from ai import AI
from player import Player


class Game():
    def __init__(self):
        self.human = Human()
        self.human_two = Human()
        self.ai = AI()
        self.goes_first = ''

    def run_game(self):
        self.display_welcome()
        self.human = self.choose_number_of_players()
        self.ai = self.choose_ai_player()
        self.play()
        self.current_turn()
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

    def choose_number_of_players(self):
        choose_number_of_players = int(input(f"Choose number of players: (0){self.human.players[0].name}, (1){self.human.players[1].name}"))
        if choose_number_of_players == 0:
            print('You chose ONE PLAYER')
            return self.human.players[0]
        elif choose_number_of_players == 1:
            print('You chose TWO PLAYER')
            return self.human.players[1]
        else:
            print('Oops! Try again.')
            self.choose_number_of_players()

    def choose_ai_player(self):
        choose_ai_player = (input(f"Would you like to play aganist our AI player?"))
        if choose_ai_player == 'YES':
            print('You are up aganist AI')
            return
        elif choose_ai_player == 'NO':
            print('Please choose number of players or try again.')
            self.choose_number_of_players()
        else:
            print('Oops! Try again.')
            self.choose_ai_player()

    def play(self):
        first_turn = random.randint(1, 2)
        if first_turn == 1:
            print('PLAYER ONE goes first!')
            self.goes_first = "PLAYER ONE"
        if first_turn == 2:
            print('PLAYER TWO goes first!') or ('AI goes first!')
            self.goes_first = "PLAYER TWO" or "AI"

    def current_turn(self):
        while self.human.choice <=2 and self.ai.choice <=1:
            if self.goes_first == "PLAYER ONE":
                self.human.choose_gesture(self.human)
                self.human_two.choose_gesture(self.human_two) or self.ai.choose_gesture(self.ai) 
            elif self.goes_first == "PLAYER TWO" or "AI":
                self.ai.choose_gesture(self.ai) or self.human_two.choose_gesture(self.human_two)
                self.human.choose_gesture(self.human)

    def display_winner(self):