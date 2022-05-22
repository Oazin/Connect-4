﻿#-------------------------------------------------------------------------------
# Name:        Connect 4
# Purpose:     Connect 4 in console display; computer could play alone
#              or you could play against the computer
#
# Author:      Oazin
#
# Created:     13/12/2020
# Copyright:   (c) Oazin 2020
# Version:     Python 3.4
#-------------------------------------------------------------------------------

from random import randint

g=[]

def empty_grid():
    """Returns a connect 4 grid 'g' that is empty"""
    for c in range (6):
        l=[]
        for line in range (7):
            l.append(0)
        g.append(l)
    return g

print(empty_grid())

def display(g):
    """Displays the game grid with the character '.' for empty cells
       the character 'X' for player 1 and the character 'O' for player 2"""
    for l in range(5,-1,-1):
        line='|'
        for c in range(7):
            if g[l][c] == 0:
                line+='.'
            elif g[l][c] == 1:
                line+='X'
            else:
                line+='O'
            line+='|'

        print(line)
    print('\n')

def move_possible(g,c):
    """Returns a boolean indicating whether it is possible to play in column 'c' and returns a boolean"""
    for l in range (6):
        if g[l][c] == 0:
            return True
    return False

def play(g,j,c):
    """Allows player 'j' to make a move in column 'c' """
    for l in range (6):
        if g[l][c]==0:
            g[l][c]=j
            break
    return g

def horiz (g, j):
    """Checks if player 'j' has four pieces alined horizontally and returns a boolean if so"""
    for l in range(6):
        for c in range (4):
            if g[l][c]==j and g[l][c+1]==j and g[l][c+2]==j and g[l][c+3]==j:
                return True


def vert (g, j):
    """Checks if player 'j' has four vertically alined pieces and returns a boolean if it is the case"""
    for c in range(7):
        for l in range(3):
            if g[l][c]==j and g[l+1][c]==j and g[l+2][c]==j and g[l+3][c]==j:
                return True

def diag(g,j):
    """Checks if player 'j' has four diagonally alined pieces and returns a boolean if so"""
    for l in range(3):
        for c in range(4):
            if g[l][c]==j and g[l+1][c+1]==j and g[l+2][c+2]==j and g[l+3][c+3]==j:
                return True
    for l in range(3):
        for c in range(6,2,-1):
            if g[l][c]==j and g[l+1][c-1]==j and g[l+2][c-2]==j and g[l+3][c-3]==j:
                return True


def victory(g,j):
    """Stops the game if any of the horiz, green or diag functions return True and if so then player 'j' has won and displays who has won"""
    if horiz(g,j)==True or vert(g,j)==True or diag(g,j)==True:
        print("Le joueur",str(j), "a gagne")
        return True

def stalemate(g):
    """Stop the game if the grid 'g' is completely filled and no one has won, which means that the game is a draw"""
    if g[5][0]!=0 and g[5][1]!=0 and g[5][2]!=0 and g[5][3]!=0 and g[5][4]!=0 and g[5][5]!=0 and g[5][6]!=0 :
        print("Stalemate")
        return True


def random_move(g,j):
    """Plays a possible random move for player 'j """
    c=randint(0,6)
    while move_possible(g,c)==False:
        c=randint(0,6)
    return c

def computer_plays_alone():
    """The computer plays randomly, in turn, displaying the grid after each move, and stops when a player wins or the game is drawn."""
    empty_grid ()
    while stalemate(g) !=True:
        for j in range(1,3,1):
            c=random_move(g,j)
            while move_possible(g,c)==False:
                    c=random_move(g,j)
            play(g,j,c)
            display(g)
            if victory(g,j)==True:
                exit()


def user_vs_comp():
    """The user to play against the computer which plays randomly, displaying the grid after each move and the result at the end of the game"""
    empty_grid()
    while stalemate(g)!=True:
        for j in range(1,3,1):
            if j==1:
                c=random_move(g,j)
                while move_possible(g,c)==False:
                    c=random_move(g,j)
                play(g,j,c)
                display(g)
            if victory(g,j)==True:
                exit()
            elif j==2:
                c=int(input("Dans quelle colonne voulez-vous placer"))
                while move_possible(g,c)==False:
                    c=int(input("Dans quelle colonne voulez-vous placer"))
                play(g,j,c)
                display(g)
            if victory(g,j)==True:
                exit()

print(computer_plays_alone())
#print(user_vs_comp())