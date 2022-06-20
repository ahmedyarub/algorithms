class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        lmap, result = defaultdict(list), dict()

        for word in words:
            lmap[len(word)].append(word)

        for ln in lmap.keys():
            lwords = lmap[ln]
            if ln <= 3:
                for lword in lwords:
                    result[lword] = lword
                continue

            def encode(group: List[str], start: int):
                nonlocal ln

                if start != 0 and len(group) == 1:
                    result[group[0]] = group[0][0] + str((len(group[0]) - 2)) + group[0][-1] if start == -1 else group[
                                                                                                                     0][
                                                                                                                 :start] + str(
                        (len(group[0]) - start - 1)) + group[0][-1]
                    return

                if start > ln - 4:
                    for word in group:
                        result[word] = word
                    return

                prefmap = defaultdict(list)
                for word in group:
                    prefmap[word[start]].append(word)

                for nxgroup in prefmap.values():
                    encode(nxgroup, start + 1)

                return

            encode(lwords, -1)

        return list(map(result.get, words))
