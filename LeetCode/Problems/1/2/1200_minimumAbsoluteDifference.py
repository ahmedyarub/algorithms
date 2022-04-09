class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        result = []
        min_dif = float('inf')
        for i in range(len(arr) - 1):
            cur_dif = arr[i + 1] - arr[i]

            if cur_dif == min_dif:
                result.append([arr[i], arr[i + 1]])
            elif cur_dif < min_dif:
                min_dif = cur_dif
                result = [[arr[i], arr[i + 1]]]

        return result
