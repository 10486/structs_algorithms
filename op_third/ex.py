import numpy as np


def allowPath(X, Y, board, currentStep=1):

    if X < 0 or X >= len(board):
        return False
    if Y < 0 or Y >= len(board[0]):
        return False
    if board[X, Y] != 0:
        return False

    board[X, Y] = currentStep
    if (len(board[board == 0]) == 0):
        return True

    NewStep = currentStep+1

    def NextStep(X, Y, variant):
        operation = {
            0: lambda X, Y: (X+1, Y+2),
            1: lambda X, Y: (X+2, Y+1),
            2: lambda X, Y: (X+2, Y-1),
            3: lambda X, Y: (X+1, Y-2),
            4: lambda X, Y: (X-1, Y-2),
            5: lambda X, Y: (X-2, Y-1),
            6: lambda X, Y: (X-2, Y+1),
            7: lambda X, Y: (X-1, Y+2),
        }
        return operation[variant](X, Y)

    for StepVariant in range(8):
        NewX, NewY = NextStep(X, Y, StepVariant)
        if allowPath(NewX, NewY, board, NewStep):
            return True
    else:
        board[X, Y] = 0
        return False


def main(h, w, startX, startY):
    board = np.zeros((h, w), dtype=int)
    res = allowPath(startX, startY, board)
    if res:
        return board
    return False


print(main(6, 6, 1, 1))
