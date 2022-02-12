def solution(l, fares):
    rides = ["UberX", "UberXL", "UberPlus", "UberBlack", "UberSUV"]
    for i in reversed(range(len(fares))):
        if fares[i] * l <= 20:
            return rides[i]
