class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def conv(time_str: str) -> int:
            return int(time_str[3:5]) + int(time_str[0:2]) * 60

        return conv(event1[0]) <= conv(event2[1]) and conv(event1[1]) >= conv(event2[0])
