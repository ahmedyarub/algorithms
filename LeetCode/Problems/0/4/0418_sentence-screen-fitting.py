class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        cnt, col, row, wi, rem = 0, 0, 0, 0, False
        s_len = len(" ".join(sentence)) + 1
        while row < rows:
            # print(col)
            if wi == 0:
                jmp = (cols - col) // s_len
                if jmp > 0:
                    cnt += jmp
                    col += jmp * s_len

            if cols - col >= len(sentence[wi]):
                col += len(sentence[wi]) + 1

                wi += 1

                if wi == len(sentence):
                    wi = 0
                    cnt += 1
            else:
                if wi == 0 and not rem:
                    rem = True
                    cnt = (rows // (row + 1)) * cnt
                    row = rows - rows % (row + 1)
                else:
                    row += 1

                col = 0

        return cnt
