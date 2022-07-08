
#Pre Order

#Iterative
def preorderTraversal(self, root: TreeNode) -> List[int]:
    if not root:
        return []
    s = [root]
    out = []
    while s:
        curr= s.pop()
        out.append(curr.val)
        if curr.right:
            s.append(curr.right)
        if curr.left:
            s.append(curr.left)
    return out

 
#In Order

#Iterative  
def inorderTraversal(self, root: TreeNode) -> List[int]:
    s = []
    curr= root
    out= []
    while s or curr:
        while curr:
            s.append(curr)
            curr= curr.left
        node= s.pop()
        out.append(node.val)
        curr = node.right
    return out
  
  
#Post Order

#Iterative
def postorderTraversal(self, root: TreeNode) -> List[int]:
    if not root:
        return []
    s = []
    node = root
    res = []
    prev=  None
    while s or node:
        while node:
            s.append(node)
            node = node.left
        peek = s[-1]
        if peek.right == None or prev == peek.right:
            res.append(s.pop().val)
            prev = peek
        else:
            prev = node
            node = peek.right
    return res
