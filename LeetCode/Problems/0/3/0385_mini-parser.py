class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        def nestedInteger():
            nonlocal s
            num = ''
            while s[-1] in '1234567890-':
                num += s.pop()
            if num:
                return NestedInteger(int(num))
            s.pop()
            lst = NestedInteger()
            while s[-1] != ']':
                lst.add(nestedInteger())
                if s[-1] == ',':
                    s.pop()
            s.pop()
            return lst

        s = list(' ' + s[::-1])
        return nestedInteger()
