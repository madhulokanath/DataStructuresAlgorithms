#Big Data Engineer

#1. SQL question on Agregation
#2. SQL question on partition by

# Data structures
# Validate a BST

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

#method 1 - recursion 

def ValidateBST(Node):
    lower=-float('inf')
    upper=float('inf')
    return helper(Node,lower,upper)


def helper(Node,lower,upper):
    if not Node:
        return True

    if lower >= Node.val or upper <= Node:
        return False

    if not helper(Node.left,lower,Node.val):
        return False
    if not helper(Node.right,Node.val,upper):
        return False
    return True

#Method 2 - When you traverse a BST inorder its a sorted list, 

def ValidateBST(Node):
    stack=[]
    inorder=-float('inf')
    while stack or Node:
        while Node:
            stack.append(Node)
            Node=Node.left
    Node=stack.pop()
    if Node.val < inorder:
        return False
    inorder=Nodel.val
    Node=Node.right
    return True

#Problem 2 Reverse the words in a sentence

#eg : " This is Coder Pad" --> "Pad Coder is This"

def reverse(s):
    s=s.split(" ")
    s=s[: : -1]
    return ' '.join(s)

