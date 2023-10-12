class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()
        peak_index = self.find_peak_index(1, length - 2, mountain_arr)
        increasing_index = self.binary_search(0, peak_index, target, mountain_arr, False)
        if mountain_arr.get(increasing_index) == target:
            return increasing_index

        decreasing_index = self.binary_search(peak_index + 1, length - 1, target, mountain_arr, True)
        if mountain_arr.get(decreasing_index) == target:
            return decreasing_index

        return -1

    def find_peak_index(self, low, high, mountainArr):
        while low != high:
            mid = low + (high - low) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                low = mid + 1
            else:
                high = mid
        return low

    def binary_search(self, low, high, target, mountainArr, reversed):
        while low != high:
            mid = low + (high - low) // 2
            if reversed:
                if mountainArr.get(mid) > target:
                    low = mid + 1
                else:
                    high = mid
            else:
                if mountainArr.get(mid) < target:
                    low = mid + 1
                else:
                    high = mid
        return low