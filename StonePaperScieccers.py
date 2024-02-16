import random

class Player():

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.history_of_movements = []

    def move(self):
        possible_movements = ["stone", "paper", "scissors"]
        if self.name == 'computer':
            movement = possible_movements[random.randint(0, 2)]
            print("Computer movement is:", movement)
        else:
            while True:
                print("Choose movement: stone, paper, scissors")
                movement = input()
                if movement in possible_movements:
                    break
                else:
                    print("Wrong Movement! Choose again!")

        self.history_of_movements.append(movement)
        return movement

    def change_score(self, score):
        self.score += score

    def history(self,movement):
        self.history_of_movements.append(movement)


class Game():

    def __init__(self,number_of_sets):
        print("Enter Name:")
        self.player0 = Player(input())
        self.player1 = Player('computer')
        self.number_of_sets = number_of_sets

    def battle(self, move0, move1):
        a , b = 0 , 0
        if move0 == move1:
            a , b =  0 , 0
        elif move0 == "stone" and move1 == "paper":
            a , b =  0,1
        elif move0 == "paper" and move1 == "stone":
            a , b =  1,0
        elif move0 == "stone" and move1 == "scissors":
            a , b =  1,0
        elif move0 == "scissors" and move1 == "stone":
            a , b =  0,1
        elif move0 == "paper" and move1 == "scissors":
            a , b =  0,1
        elif move0 == "scissors" and move1 == "paper":
            a , b =  1,0

        if a < b:
            print("You lost this set!")
        elif a>b:
            print("You won this set!")
        else:
            print("Nothing!")

        self.player0.change_score(a)
        self.player1.change_score(b)

    def play(self):
        while self.number_of_sets >0:
            self.battle(self.player0.move(), self.player1.move())
            self.number_of_sets -=1
        self.final_result()

    def final_result(self):
        print("Your score is: ", self.player0.score)
        print("Your rival score is: ", self.player1.score)
        if self.player0.score == self.player1.score:
            print("No one won!")
        elif self.player1.score > self.player0.score:
            print("Loser!")
        elif self.player1.score<self.player0.score:
            print("Congrats! You won the game!")

if __name__ == "__main__":
    print("Enter number of sets to play: ")
    number_of_sets = int(input())
    game = Game(number_of_sets)
    game.play()
















#%%
