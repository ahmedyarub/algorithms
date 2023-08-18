class Solution:
    def houseCount(self, street: Optional['Street'], k: int) -> int:
        for i in range(0, k):
            street.closeDoor()
            street.moveLeft()

        result = 1
        street.openDoor()
        street.moveLeft()

        while not street.isDoorOpen():
            street.moveLeft()
            result += 1

        return result
