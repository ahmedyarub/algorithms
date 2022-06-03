class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        result, prev, mx = set(), 0, 0

        for r, k in zip(releaseTimes, keysPressed):
            dif = r - prev
            if dif > mx:
                mx = dif
                result = {ord(k)}
            elif dif == mx:
                result.add(ord(k))

            prev = r

        return chr(max(result))
