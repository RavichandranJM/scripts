#! /usr/bin/python

def rock_paper_scissor():
    print("Rock Paper Scissor game")
    print("Enter R for Rock, P for Paper, S for Scissor")
    #print("Player1:")
    p1 = raw_input("Player1:")
    p2 = raw_input("Player2:")
    if p1 == p2:
        print("Draw")
    elif p1 == 'R' and p2 == 'S':
        print("Player1 wins")
    elif p1 == 'S' and p2 == 'P':
        print("Player1 wins")
    elif p1 == 'P' and p2 == 'R':
        print("Player1 wins")
    else:
        print("Player2 wins")
while True:
    rock_paper_scissor()
    q = raw_input("Play again?(y/n):")
    if q in 'Yy':
        continue
    else:
        break



