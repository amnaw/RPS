import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, player_previous_move, their_move):
        self.player_previous_move = player_previous_move
        self.their_move = their_move

    def __init__(self):
        self.their_move = moves[random.randint(0, 2)]

        self.player_previous_move = moves[random.randint(0, 2)]

        self.score = 0


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class RandomPlayer(Player):
    def move(self):
        return moves[random.randint(0, 2)]


class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("'rock','paper','scissors'>? ").lower()
            if move == "rock" or move == "paper" or move == "scissors":
                return move
            else:
                print(" please enter a valid choice.")


class ReflectPlayer(Player):
    def move(self):
        return self.their_move


class CyclePlayer(Player):
    def move(self):
        if self.player_previous_move == "rock":
            return "paper"
        if self.player_previous_move == "paper":
            return "scissors"
        if self.player_previous_move == "scissors":
            return "rock"


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.scores = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        if beats(move1, move2):
            self.p1.score += 1
            print("     player one wins")

        elif move1 == move2:
            # p1.score += 0
            # p2.score += 0
            print("          tie")
        else:
            self.p2.score += 1
            print("    player two wins")

        print(f"Player one : {self.p1.score} Player two : {self.p2.score}")

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")

        if self.p1.score > self.p2.score:
            print(" ** PLAYER ONE WINS ** ")
        elif self.p2.score > self.p1.score:
            print(" ** PLAYER TWO WINS **")
        else:
            print("** PLAYER TWO TIES WITH PLAYER ONE **")

        print("THE FINAL SCORES ARE :")
        print(f"PLAYER 1 :{self.p1.score}")
        print(f"PLAYER 2 :{self.p2.score}")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
