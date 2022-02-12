def checkPark(x1, y1, x2, y2, parkingLot):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if parkingLot[i][j] == 1:
                return False

    return True


def solution(carDimensions, parkingLot, luckySpot):
    if luckySpot[2] - luckySpot[0] + 1 == carDimensions[1]:
        return checkPark(luckySpot[0], 0, luckySpot[2], luckySpot[3], parkingLot) or \
               checkPark(luckySpot[0], luckySpot[1], luckySpot[2], len(parkingLot[0]) - 1, parkingLot)

    if luckySpot[3] - luckySpot[1] + 1 == carDimensions[1]:
        return checkPark(0, luckySpot[1], luckySpot[2], luckySpot[3], parkingLot) or \
               checkPark(luckySpot[0], luckySpot[1], len(parkingLot) - 1, luckySpot[3], parkingLot)
