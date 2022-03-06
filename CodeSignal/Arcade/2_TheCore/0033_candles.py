def solution(solutionNumber, makeNew):
    return solutionNumber + (solutionNumber - 1) // (makeNew - 1)
