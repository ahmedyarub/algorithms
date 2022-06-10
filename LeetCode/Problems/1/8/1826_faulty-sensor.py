class Solution:
    def badSensor(self, sensor1: List[int], sensor2: List[int]) -> int:
        n = len(sensor1)
        for i in range(n):
            if sensor1[i] != sensor2[i]:
                break
        j = k = i
        while j < n - 1 and sensor1[j] == sensor2[j + 1]:
            j += 1
        while k < n - 1 and sensor1[k + 1] == sensor2[k]:
            k += 1

        return -1 if k == n - 1 and j == n - 1 else 1 if j == n - 1 else 2
