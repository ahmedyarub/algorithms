def solution(cell1, cell2):
    return not sum(map(ord, cell1 + cell2)) % 2
