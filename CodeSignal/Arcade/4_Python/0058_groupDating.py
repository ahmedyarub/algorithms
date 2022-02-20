def solution(male, female):
    return [m for i, m in enumerate(male) if m != female[i]], [f for i, f in enumerate(female) if f != male[i]]
