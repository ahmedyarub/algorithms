def solution(inputArray):
    moves = 0

    for i in range(1, len(inputArray)):
        additional_moves = 0
        if inputArray[i] <= inputArray[i - 1]:
            additional_moves = inputArray[i - 1] - inputArray[i] + 1

        moves += additional_moves
        inputArray[i] += additional_moves

    return moves
