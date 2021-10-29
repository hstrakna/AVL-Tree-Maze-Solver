class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.depth = 0
        self.depthTotal = 0
        self.nodeCount = 0
        self.SRCount = 0
        self.DRCount = 0

class AVLTree(object):
    def insertNode(self, root, newNode):
        if not root:
            return Node(newNode)
        elif newNode < root.val:
            root.left = self.insertNode(root.left, newNode)
        elif newNode > root.val:
            root.right = self.insertNode(root.right, newNode)

        # set the root's height to the maximum of its children plus one
        # root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        root.depth = 1 + max(self.getDepth(root.left), self.getDepth(root.right))



        if self.getDepth(root) > self.getDepth(root.right) + 1 and newNode < root.left.val:
            root.SRCount += 1
            return self.zag(root)

        if self.getDepth(root) > self.getDepth(root.right) + 1 and newNode < root.left.val:
            root.DRCount += 1
            root.left = self.zig(root.left)
            return self.zag(root)

        if self.getDepth(root) > self.getDepth(root.left) + 1 and newNode > root.right.val:
            root.SRCount += 1
            return self.zig(root)

        if self.getDepth(root) > self.getDepth(root.left) + 1 and newNode < root.right.val:
            root.DRCount += 1
            root.right = self.zag(root.right)
            return self.zig(root)

        root.depthTotal += root.depth
        root.nodeCount += 1
        print(root.depth)
        return root



    def zig(self, b):
        # set node a to b's right child
        a = b.right
        # get a's left child and set it to childLeft
        childLeft = a.left

        # swtich a's left child to b
        a.left = b
        # switch b's right child to a's left child
        b.right = childLeft

        # set b's height to the maximum of its children plus one
        b.depth = max(self.getDepth(b.left), self.getDepth(b.right)) + 1
        a.depth = max(self.getDepth(a.left), self.getDepth(a.right)) + 1
        # return new root
        return a

    # do the inverse of the zig operation
    def zag(self, b):
        a = b.left
        childRight = a.right

        a.right = b
        b.left = childRight

        b.depth = max(self.getDepth(b.left), self.getDepth(b.right))
        a.depth = max(self.getDepth(a.left), self.getDepth(a.right))

        return a

    def getDepth(self, root):
        if not root:
            return 0
        return root.depth

    def avgDepth(self):
        if not root:
            return 0
        avg = root.depthTotal // root.nodeCount
        return avg

    def singleRotationCount(self):
        return root.SRCount

    def doubleRotationCount(self):
        return root.DRCount


myTree = AVLTree()
root = None

root = myTree.insertNode(root, 10)
root = myTree.insertNode(root, 20)
root = myTree.insertNode(root, 30)
root = myTree.insertNode(root, 40)
root = myTree.insertNode(root, 25)
root = myTree.insertNode(root, 50)


avgDepth = myTree.avgDepth()
DR = myTree.doubleRotationCount()
SR = myTree.singleRotationCount()
print("Avg. Depth: {}".format(avgDepth))
print("Single rotations: {}".format(SR))
print("Double rotations: {}".format(DR))

