class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        smap = defaultdict(set)
        for sp in similarPairs:
            smap[sp[0]].add(sp[1])
            smap[sp[1]].add(sp[0])

        for w1, w2 in zip(sentence1, sentence2):
            if w1 != w2 and w1 not in smap[w2]:
                return False

        return True
