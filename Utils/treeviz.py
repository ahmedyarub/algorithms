from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def arrayToLinkedList(arr: List, cycle: int = None) -> Optional[ListNode]:
    head: ListNode = None
    prev: ListNode = head
    cycle_node: ListNode = None
    cnt: int = 0

    for item in arr:
        node = ListNode(item)

        if cycle is not None and cnt == cycle:
            cycle_node = node

        cnt += 1

        if not head:
            head = node
        else:
            prev.next = node
        prev = node

    if cycle_node:
        prev.next = cycle_node

    return head


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)


def stringToTree(string: str) -> Optional[TreeNode]:
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root


def getTreeNode(root: TreeNode, val: int) -> Optional[TreeNode]:
    queue = [root]

    while queue:
        node = queue.pop()

        if node.val == val:
            return node

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return None


def drawtree(root: TreeNode):
    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else -1

    def jumpto(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()

    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jumpto(x, y - 20)
            t.write(node.val, align='center', font=('Arial', 12, 'normal'))
            draw(node.left, x - dx, y - 60, dx / 2)
            jumpto(x, y - 20)
            draw(node.right, x + dx, y - 60, dx / 2)

    import turtle
    t = turtle.Turtle()
    t.speed(0)
    turtle.delay(0)
    h = height(root)
    jumpto(0, 30 * h)
    draw(root, 0, 30 * h, 40 * h)
    t.hideturtle()
    turtle.mainloop()


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
