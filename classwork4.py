'''
    Zhang Junyan, 1129832
    Lin Qingxin, 1098238
'''
# Define a node class that has left and  right sides
class Node:
    def __init__(self, Node_value):
        self.left = None    # left side node (leaf)
        self.right = None   #right side node (leaf)
        self.Node_value = Node_value   # actual node value
# Define a function to insert Node_value in to the tree
    def insert(self, Node_value):
# Compare the new value with the parent node
        if self.Node_value:   # if there is a root node      
            if Node_value < self.Node_value:  # if the value that we need to insert is less than root value
                if self.left is None:     # if no left side node exist
                    self.left = Node(Node_value) # create a left side node
                else:                      # otherwise (means there is an empty left node)
                    self.left.insert(Node_value)  # put that value in the left of the existing node
            elif Node_value > self.Node_value:          # do the same thing for the right side node if >    
                if self.right is None:
                    self.right = Node(Node_value)
                else:
                    self.right.insert(Node_value)
        else:        # if no root exists
            self.Node_value = Node_value     # put the value in the root

# Printing the binary tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.Node_value),
        if self.right:
            self.right.PrintTree()
    # Define the search function, and after each search operation there will be a count
    def  search(root,Node_value):
        '''
            para self for compare root and its left&right child
            count for count steps
            If the value of the keyword is equal to the value of node, it returns.
            If it is less than, it looks for the left; otherwise, it looks for the right
            Return: search node or none
        '''
        self = root
        count = 0
        # When BST has nodes, then go to search
        while self is not None:
            count = count +1 #step +1 
            if self.Node_value == Node_value:
                print("Search",str(Node_value),"in",str(count),"step")
                return self.Node_value
            elif self.Node_value < Node_value:
                self = self.right
            else:
                self = self.left
        # Otherwise, the BST doesn't contain the value
        print("There has no",str(Node_value))
        
# Define main to make a node object and call inser and print functions
def main():
    my_BST = Node(10)   # creat an object from the node class, I called it my_BST.
    print("The BST contains:")
    my_BST.insert(1)
    my_BST.insert(12)
    my_BST.insert(3)
    my_BST.insert(6)
    my_BST.PrintTree()
    # Search below nodes:1,6,9
    my_BST.search(1)
    my_BST.search(6)
    my_BST.search(9)
if __name__ == "__main__":
   main()

