#!/usr/bin/env python3
# Author: Stephen Moon
# TODO:
# 1. Validate user entries and seizes upon user mistakes
#    such as putting X in one location more than once
# 2. Allow a user to start first or second
# 3. Perhaps re-write using class
# 4. Record user moves
# 

board = [' ' for x in range(10)]


def insertLetter(letter: str, pos: int) -> None:
    board[pos] = letter


def spaceIsFree(pos: str) -> bool:
    return board[pos == ' ']


def printBoard(board: list) -> None:
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('__________')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('__________')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


def isWinner(board: list, letter: str) -> bool:
    return (board[7] == letter and board[8] == letter and board[9] == letter) or \
        (board[4] == letter and board[5] == letter and board[6] == letter) or \
        (board[1] == letter and board[2] == letter and board[3] == letter) or \
        (board[1] == letter and board[4] == letter and board[7] == letter) or \
        (board[2] == letter and board[5] == letter and board[8] == letter) or \
        (board[3] == letter and board[6] == letter and board[9] == letter) or \
        (board[1] == letter and board[5] == letter and board[9] == letter) or \
        (board[3] == letter and board[5] == letter and board[7] == letter)


def playerMove() -> None:
    run = True
    while run:
        move = input("Please select a position to a place an 'X' (1-9): ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')


def selectRandom(lst: list) -> int:
    import random
    length = len(lst)
    print(f"Length of list: {length}")
    r = random.randrange(0, length)
    return lst[r]


def computerMove() -> int:
    possibleMoves = [index for index, letter in enumerate(
        board) if letter == ' ' and index != 0]
    # possible moves are 1 to 9
    move = 0 # not a possible move.  it implies a tied game

    for letter in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]  # makes a copy not reference
            # print(f"Computer boardCopy: {boardCopy[1:]}")
            boardCopy[i] = letter
            print(f"Computer boardCopy: {boardCopy[1:]}, letter: {letter}")
            if isWinner(boardCopy, letter):
                print(f"USER {letter} IS a winner if Computer does NOT block {letter} at Index {i}")
                move = i
                return move
           
    if 5 in possibleMoves:
        print(f"The center of the grid IS open.")
        move = 5
        return move
    else:
        print(f"The center of the grid is NOT open.")

    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        print(f"Cornersopen: {cornersOpen}")
        move = selectRandom(cornersOpen)
        return move
    else:
        print(f"NO corners are open")

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        print(f"EdgesOpen: {edgesOpen}")
        move = selectRandom(edgesOpen)
    else:
        print(f"NO edges are open")

    return move


def isBoardFull(board: list) -> bool:
    if board.count(' ') > 1:
        return False
    else:
        return True


def main() -> None:
    print("Welcome to Crystal's tic tac toe!")
    printBoard(board)

    while not (isBoardFull(board)):
        if not (isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print("Sorry, O's WON this time!")
            break

        if not (isWinner(board, 'X')):
            move = computerMove()
            if move == 0:
                print('Tie Game!')
            else:
                insertLetter('O', move)
                print("Computer places an 'O' in position", move, ":")
            printBoard(board)
        else:
            print("Sorry, X's WON this time! Very nice job, Crystal!")
            break

    if isBoardFull(board):
        print('The game is tied!')


if __name__ == '__main__':
    main()
