class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parents = []

        def find(node: int) -> int:
            if parents[node] == node:
                return node
            else:
                return find(parents[node])

        def union(i: int, j: int):
            rep_i, rep_j = find(i), find(j)

            parents[rep_j] = rep_i

        for i in range(len(accounts)):
            parents.append(i)

        email_groups = {}
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                name, email = accounts[i][0], accounts[i][j]

                if email not in email_groups:
                    email_groups[email] = i
                else:
                    union(email_groups[email], i)

        results = defaultdict(set)
        for i, parent in enumerate(parents):
            results[find(parent)].update(accounts[i][1:])

        return [[accounts[parent][0]] + sorted(emails) for parent, emails in results.items()]
