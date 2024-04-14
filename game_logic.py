from card_logic import *

def checkWinner(player):
    if len(player) == 0:
        print("Game has ended")
        return True

def updateBoard(p):
    print(p)

def takeTurn(p1Cards, p2Cards):
    while True:
        try:
            p1 = int(input("Player 1, Enter your card: "))
            p1Cards = calculateGame(p1Cards, p1)
            updateBoard(p1Cards)
            if checkWinner(p1Cards):
                break

            p2 = int(input("Player 2, Enter your card: "))
            p2Cards = calculateGame(p2Cards, p2)
            updateBoard(p2Cards)
            if checkWinner(p2Cards):
                break

        except:
            print("Your input is incorrect, please try again")

