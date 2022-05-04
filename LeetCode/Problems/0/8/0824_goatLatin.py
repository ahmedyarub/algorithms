class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        result = []
        vowels = ['a', 'e', 'i', 'o', 'u']

        for i, word in enumerate(sentence.split()):
            if word[0].lower() in vowels:
                result.append(word + "ma" + "a" * (i + 1))
            else:
                result.append(word[1:] + word[0] + "ma" + "a" * (i + 1))

        return " ".join(result)
