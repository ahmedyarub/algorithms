class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        queue, result, cur_level, cur_list = [(root, 0)], [], 0, []

        while queue:
            node, node_level = queue.pop(0)

            if node_level != cur_level:
                result.append(cur_list)
                cur_list = []
                cur_level = node_level

            cur_list.append(node.val)

            queue.extend([(c, cur_level + 1) for c in node.children])

        return result + [cur_list]
