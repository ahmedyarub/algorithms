def solution(name):
    if re.match('[a-z_][0-9_a-z]*$', name, re.IGNORECASE):
        return True
    return False
