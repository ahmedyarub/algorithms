class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        mp = Counter(list(s))
        if len([cnt for cnt in mp.values() if cnt % 2]) > 1:
            return []

        def palindrome() -> List[str]:
            nonlocal mp

            result = []
            for ch in mp.keys():
                if mp[ch] >= 2:
                    mp[ch] -= 2
                    result.extend([ch + pal + ch for pal in palindrome()])
                    mp[ch] += 2

            if not result:
                for ch in mp.keys():
                    if mp[ch] == 1:
                        return [ch]

                return ['']
            else:
                return result

        return palindrome()
