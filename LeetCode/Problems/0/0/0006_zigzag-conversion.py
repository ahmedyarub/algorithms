class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        n = len(s)
        cycle = 2 * numRows - 2
        strlist = []
        for i in range(numRows):
            for j in range(i, n, cycle):
                strlist.append(s[j])
                if i != numRows - 1 and i != 0 and j + cycle - 2 * i < n:
                    strlist.append(s[j + cycle - 2 * i])

        return ''.join(strlist)
