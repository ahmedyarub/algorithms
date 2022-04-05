class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        iw, ia = 0, 0
        while ia < len(abbr) and iw < len(word):
            if '9' >= abbr[ia] > '0':
                c = ""
                while ia < len(abbr) and '9' >= abbr[ia] >= '0':
                    c += abbr[ia]
                    ia += 1

                iw += int(c)
            else:
                if word[iw] != abbr[ia]:
                    return False

                iw += 1
                ia += 1

            if iw > len(word):
                return False

        return iw == len(word) and ia == len(abbr)
