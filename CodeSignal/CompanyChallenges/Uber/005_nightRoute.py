def solution(city):
    distances = [255] * len(city)

    for i in range(1, len(city)):
        calcDistances(distances, city, 0, 0, i)

    return distances[len(city) - 1]


def calcDistances(distances, city, prevDistance, fromIndex, toIndex):
    cur_distance = city[fromIndex][toIndex]
    if cur_distance == -1:
        return

    new_distance = prevDistance + cur_distance
    if new_distance < distances[toIndex]:
        distances[toIndex] = new_distance

        for i in range(len(city)):
            calcDistances(distances, city, new_distance, toIndex, i)
