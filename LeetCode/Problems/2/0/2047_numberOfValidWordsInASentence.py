class Solution:
    def countValidWords(self, sentence: str) -> int:
        pattern = re.compile(r'^([a-z]+\-?[a-z]+[!\.,]?)$|^([a-z]*[!\.,]?)$')
        count = 0

        for word in sentence.split():
            if re.match(pattern, word):
                count += 1

        return count
