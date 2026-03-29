from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def insert(root, val):
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root


def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def postorder(root):
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]


def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)


def level_order(root):
    if not root:
        return []

    queue = deque([root])
    result = []

    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result


def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def is_same(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False

    return (p.val == q.val and
            is_same(p.left, q.left) and
            is_same(p.right, q.right))


root = None

while True:
    print("\n1.insert\n2.inorder\n3.postorder\n4.preorder\n5.levelorder\n6.maxdepth\n7.exit\n")
    choice = int(input("enter your choice:"))

    if choice == 1:
        val = int(input("Enter value: "))
        root = insert(root, val)

    elif choice == 2:
        print("Inorder:", inorder(root))

    elif choice == 3:
        print("Postorder:", postorder(root))

    elif choice == 4:
        print("Preorder:", preorder(root))

    elif choice == 5:
        print("Level Order:", level_order(root))

    elif choice == 6:
        print("Max Depth:", max_depth(root))

    elif choice == 7:
        break

    else:
        print("Invalid Choice")