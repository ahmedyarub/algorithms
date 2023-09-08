class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        items = sorted([(freq, ch) for ch, freq in Counter(s).items()])
        maxFreq = items[-1][0]
        slots, slot = ["" for _ in range(maxFreq)], 0

        while items:
            freq, ch = items.pop()
            if freq == maxFreq:
                for i in range(maxFreq):
                    slots[i] = slots[i] + ch
            else:
                while freq:
                    slot = slot % (maxFreq - 1)
                    slots[slot] = slots[slot] + ch
                    freq -= 1
                    slot += 1

        for i in range(maxFreq - 1):
            if len(slots[i]) < k:
                return ""

        return "".join(slots)
