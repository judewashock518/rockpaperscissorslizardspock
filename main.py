

from game import Game
if __name__ == '__main__':
    game_map = {0:"rock", 1:"paper", 2:"scissors", 3:"lizard", 4:"spock"}

    rpsls_table = [[-1,1,0,0,4], [1,-1,2,3,1], [0,2,-1,2,4], [0,3,2,-1,3], [4,1,4,3,-1]]

    game = Game()
    game.run_game()
