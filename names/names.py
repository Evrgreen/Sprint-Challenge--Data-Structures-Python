import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

# inital implementation 1.26 seconds
# for name in names_1:
#     if name in names_2:
#         duplicates.append(name)

#  Attempted AVLtree failed
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
#         self.height = 1


# class AVLTree:
#     def __init__(self):
#         self.root = None

#     def insert(self, root, value):
#         if not root:
#             print('adding root', value)
#             return Node(value)
#         elif value < root.val:
#             root.left = self.insert(root.left, value)
#         elif value > root.val:
#             root.right = self.insert(root.right, value)
#         root.height = 1 + max(self.getHeight(root.left),
#                               self.getHeight(root.right))
#         balance = self.getBalance(root)
#         if balance > 1 and value < root.left.val:
#             return self.leftRotate(root)
#         if balance < -1 and value > root.left.val:
#             return self.rightRotate(root)
#         if balance > 1 and value > root.left.val:
#             root.left = self.leftRotate(root.left)
#             return self.rightRotate(root)
#         if balance < -1 and value < root.right.val:
#             root.right = self.rightRotate(root.right)
#             return self.leftRotate(root)
#         print(root.val)
#         return root

#     def leftRotate(self, node):
#         newRoot = node.right
#         lowLeft = newRoot.left
#         newRoot.left = node
#         node.right = lowLeft

#         node.height = 1 + max(self.getHeight(node.left),
#                               self.getHeight(node.right))
#         newRoot.height = 1 + \
#             max(self.getHeight(newRoot.left), self.getHeight(newRoot.right))
#         return newRoot

#     def rightRotate(self, node):
#         newRoot = node.left
#         lowright = newRoot.right
#         newRoot.right = node
#         node.right = lowright

#         node.height = 1 + max(self.getHeight(node.left),
#                               self.getHeight(node.right))
#         newRoot.height = 1 + \
#             max(self.getHeight(newRoot.left), self.getHeight(newRoot.right))
#         return newRoot

#     def getHeight(self, node):
#         if not node:
#             return 0
#         return node.height

#     def getBalance(self, root):
#         if not root:
#             return 0
#         return self.getHeight(root.left) - self.getHeight(root.right)

#     def preOrder(self, root):
#         if not root:
#             return
#         print(f'{root.val}', end="")
#         self.preOrder(root.left)
#         self.preOrder(root.left)

#     def contains(self, node, value):
#         if not node:
#             return
#         if node.value == value:
#             return value
#         if not node.next:
#             return False
#         else:
#             if node.value < value:
#                 return self.contains(node.right)
#             self.contains(node.left)


# nameTree = AVLTree()
# root = None
# for name in names_1:
#     root = nameTree.insert(root, name)
#     print(root.val)
# for name in names_2:
#     if nameTree.contains(nameTree, name):
#         duplicates.append(name)

# Optimization 1 turning files into sets and then finding the intersections .006 seconds
for name in set(names_1).intersection(set(names_2)):
    duplicates.append(name)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
