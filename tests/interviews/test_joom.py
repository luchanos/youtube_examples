class Node:
    def __init__(self, value, left: "Node" = None, right: "Node" = None):
        self.value = value
        self.left = left
        self.right = right


def is_bst(node: Node):
    res = True
    res_1 = True

    if node.left is None and node.right is None:
        return True

    if node.right is not None and node.left is not None:
        if node.value < node.left.value or node.value > node.right.value:
                return False
        res = is_bst(node.left)
        res_1 = is_bst(node.right)

    elif node.left is None:
        if node.value > node.right.value:
            return False
        res = is_bst(node.right)

    elif node.right is None:
        if node.value < node.left.value:
            return False
        res_1 = is_bst(node.left)

    return res and res_1
