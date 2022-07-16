class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms, last_r = [], 0

        for interval in sorted(intervals):
            r, cnt, found = last_r, 0, False
            while not found and cnt < len(rooms):
                ri = 0
                for room_interval in rooms[r]:
                    if room_interval[0] > interval[1]:
                        found = True
                    elif room_interval[1] > interval[0]:
                        break

                    ri += 1
                if found or ri == len(rooms[r]):
                    rooms[r].insert(ri, interval)
                    last_r = r
                    found = True

                r = (r + 1) % len(rooms)
                cnt += 1

            if not found:
                rooms.append([interval])
                last_r = len(rooms) - 1

        return len(rooms)
