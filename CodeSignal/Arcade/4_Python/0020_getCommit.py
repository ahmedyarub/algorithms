def solution(commit):
    return re.sub(r'[0\?\+\!]*', '', commit)
