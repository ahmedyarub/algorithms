class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        prefs = defaultdict(list)

        for product in products:
            for i in range(len(product)):
                pref = product[:i + 1]
                if searchWord[:i + 1] == pref:
                    prefs[pref].append(product)

        for words in prefs.values():
            words.sort()

        return [prefs[searchWord[:i + 1]][:3] for i in range(len(searchWord))]
