def solution(score1, score2):
    return (7 in (score1, score2) and 7 > min(score1, score2) >= 5) or \
           (6 in (score1, score2) and min(score1, score2) < 5)
