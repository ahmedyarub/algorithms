"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""


class Node():
    val = None
    left = None
    right = None

    # define your fields here
    def evaluate(self) -> int:
        if self.val.isdigit():
            return int(self.val)

        l = self.left.evaluate()
        r = self.right.evaluate()
        match self.val:
            case '+':
                return l + r
            case '-':
                return l - r
            case '*':
                return l * r
            case '/':
                return l // r


"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""


class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        stack = []

        node = None
        for p in postfix:
            node = Node()
            node.val = p
            if not p.isdigit():
                node.right = stack.pop()
                node.left = stack.pop()
            stack.append(node)

        return node


"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
