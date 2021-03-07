class Node:

    def __init__(self, val):

        self.left = None
        self.right = None
        self.val = val
# Insert Node
    def insert(self, val):

        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = Node(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = Node(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val

# Print the Tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.val),
        if self.right:
            self.right.PrintTree()

# Inorder traversal
# Left -> Root -> Right
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.val)
            res = res + self.inorderTraversal(root.right)
        return res

# Preorder traversal
# Root -> Left -> Right
    def inorderTraversal(self, root):
        res = []
        if root:
            res.append(root.val)
            res = self.inorderTraversal(root.left)
            res = res + self.inorderTraversal(root.right)
        return res

# Postorder traversal
# Left -> Right -> Root
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res = res + self.inorderTraversal(root.right)
            res.append(root.val)
        return res
    def binaryTreePaths1(self, root):
        if not root:
            return []
        res, stack = [], [(root, "")]
        while stack:
            #print(stack)
            node, ls = stack.pop()
            if not node.left and not node.right:
                res.append(ls+str(node.val))
            if node.right:
                stack.append((node.right, ls+str(node.val)+"->"))
            if node.left:
                stack.append((node.left, ls+str(node.val)+"->"))
        return res

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
#root.PrintTree()
#print(root.inorderTraversal(root))

#print(root.binaryTreePaths1(root))

List = [1,2,3,4]
List1 = [2,4,45]

result = List + List1
#print(result)

'''
def closestLocations(totalCrates, allLocations, truckCapacity):
    # WRITE YOUR CODE HERE
    List = []
    Result = []
    for x,y in allLocations:
        List.append(x*x+y*y)
    dict = {}
    i = 0
    for x,y in allLocations:
        dict.update({i:x*x+y*y})
        i+=1
    dict.sort()
    for i in range(truckCapacity):
        Result.append()
    return Result
'''
char = ([3,6],[2,4],[5,3],[2,7],[1,8],[7,9])
#print(closestLocations(6,char,3))
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
'''

List = [[1,2]]
List.append([1,2])
print(List)

def closestLocations(totalCrates, allLocations, truckCapacity):
    # WRITE YOUR CODE HERE
    List = []
    Result = []
    for x,y in allLocations:
        List.append(x*x+y*y)
    List.sort()
    for i in range(truckCapacity):
        for x,y in allLocations:
            if x*x+y*y == List[i]:
                Result.append([x,y])
    return Result