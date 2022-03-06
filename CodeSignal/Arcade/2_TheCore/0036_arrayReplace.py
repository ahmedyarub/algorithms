def solution(inputArray, elemToReplace, substitutionElem):
    return [substitutionElem if i == elemToReplace else i for i in inputArray]
