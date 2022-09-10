class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort()
        result, mx_defense, prev_mx = 0, properties[-1][1], float('-inf')

        for i in range(len(properties) - 2, -1, -1):
            if (properties[i][0] != properties[i + 1][0] and properties[i][1] < mx_defense) or \
                    (properties[i][0] == properties[i + 1][0] and properties[i][1] < prev_mx):
                result += 1

            if properties[i][0] != properties[i + 1][0]:
                prev_mx = mx_defense
                mx_defense = max(mx_defense, properties[i][1], prev_mx)

        return result
