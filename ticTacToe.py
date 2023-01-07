"""This program plays a game of Rock,  Paper,  Scissors between two Players,
and reports both Player's scores each round."""
import random
moves = ['rock',  'paper',  'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.score = 0
        self.myMove = ''
        self.hisMove = ''

    def move(self):
        return 'rock'

    def learn(self,  my_move,  their_move):
        self.myMove = my_move
        self.hisMove = their_move


def beats(one,  two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self,  p1,  p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        p1_result = self.check_score(move1, move2)
        p2_result = self.check_score(move2, move1)
        self.score(p1_result, p2_result)
        self.p1.learn(move1,  move2)
        self.p2.learn(move2,  move1)

    def play_game(self):
        print("Game start!")
        noWinner = True
        round = 1
        while noWinner:
            print(f"Round {round}:")
            self.play_round()
            print(f'score1 = {self.p1.score} score2 = {self.p2.score}')
            round += 1
            print()
            noWinner = self.checkWinner(noWinner)
        print("final score")
        print(f'score1 = {self.p1.score} score2 = {self.p2.score}')
        print("Game over!")

    def check_score(self, move1, move2):
        return beats(move1, move2)

    def score(self, result1, result2):
        if result1 == result2:
            print('tie')
        elif result1:
            self.p1.score += 1
        elif result2:
            self.p2.score += 1

    def checkWinner(self, noWinner):
        diffrince = abs(self.p1.score-self.p2.score)
        if diffrince >= 3:
            if self.p1.score > self.p2.score:
                print('p1 wins vs p2 by ', self.p1.score, 'to', self.p2.score)
            else:
                print('p1 wins vs p2 by ', self.p2.score, 'to', self.p1.score)
            noWinner = False
        return noWinner


class RandomPlayer(Player):

    def move(self):
        choice = random.randint(1, 3)
        if choice == 1:
            return 'rock'
        elif choice == 2:
            return 'paper'
        elif choice == 3:
            return 'scissors'


class HumanPlayer(Player):
    def move(self):
        while True:
            choice = input('Enter your choice (rock ,  paper ,  scissors)')
            if choice in ['rock', 'paper', 'scissors']:
                return choice
            print('wrong input please try again')


class ReflectPlayer(Player):
    def move(self):
        if self.myMove == '':
            return 'rock'
        elif self.hisMove == 'rock':
            return 'rock'
        elif self.hisMove == 'paper':
            return 'paper'
        elif self.hisMove == 'scissors':
            return 'scissors'


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.module = 1

    def move(self):
        if self.module == 1:
            self.module += 1
            return 'rock'
        elif self.module == 2:
            self.module += 1
            return 'paper'
        else:
            self.module = 1
            return 'scissors'


if __name__ == '__main__':
    game = Game(CyclePlayer(),  RandomPlayer())
    game.play_game()
