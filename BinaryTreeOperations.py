#This program includes includes 3 operations on tree: Insert,find and traveral


class node:
    def __init__(self,val):
        self.val = val
        self.leftchild = None
        self.rightchild = None

    def insert(self,data):           #Insert in binary tree
        if self.val == data:
            return False
        elif self.val < data:
            if self.rightchild:
                return self.rightchild.insert(data)
            else:
                self.rightchild = node(data)
                return True
        else:
            if self.leftchild:
                return self.leftchild.insert(data)
            else:
                self.leftchild = node(data)
                return True

    def preorder(self):                                   #Preorder traversal
        if self:
            print(str(self.val))
            if (self.leftchild):
                self.leftchild.preorder()
            if (self.rightchild):
                self.rightchild.preorder()

    def postorder(self):                                  #Postorder traversal
        if self:
            if (self.leftchild):
                self.leftchild.postorder()
            if (self.rightchild):
                self.rightchild.postorder()
            
            print(str(self.val))

    def inorder(self):                                    #Inorder traversal  
        if self:
            if (self.leftchild):
                self.leftchild.inorder()
            print(str(self.val))
            if (self.rightchild):
                self.rightchild.inorder()
            
    def find(self,data):                                   #Finding given element
        if self.val == data:
            return True
        elif self.val > data:
            if self.leftchild:
                return self.leftchild.find(data)
            else:
                return False
        else:
            if self.rightchild:
                return self.rightchild.find(data)
            else:
                return False

class tree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = node(data)
            return True

    def preorder(self):
        self.root.preorder()

    def inorder(self):
        self.root.inorder()
        
    def postorder(self):
        self.root.postorder()
 
    def find(self,data):
        if self.root == None:
            return False
        else:
            return self.root.find(data)

bst = tree()
print ("Inserting elements:")
print(bst.insert(10))
print(bst.insert(20))
print(bst.insert(5))  

print("Inorder traversal:")
bst.inorder()
print("Preorder traversal:")
bst.preorder()
print("Postorder traversal:")
bst.postorder()

print("Result of find operation:")
print(bst.find(20))
