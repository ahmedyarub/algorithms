def solution(inputArray, elemToReplace, substitutionElem):
    return [substitutionElem if num == elemToReplace else num for num in inputArray]
