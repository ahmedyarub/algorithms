def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    return (yourLeft == friendsLeft and yourRight == friendsRight) or (
            yourLeft == friendsRight and yourRight == friendsLeft)
