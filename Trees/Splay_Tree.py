#Michael Robertson
#mirob2005@gmail.com
#Completed: 3/14/2013

# Implements a Splay Tree that uses a method called splay that rotates the tree
#   so that the most recently accessed node is on the top of the tree but
#   maintains the requirements of a BST.
# Improves the worst case search, insert, delete of a BST from O(n) to O(log n)
#   amortized.
# Inherits insertList, __str__, print methods, and Node
#   class indirectly from BST_iterative and the DFS traversals and find min/max
#   from BST_recursive

from BST_recursive import Node
from BST_recursive import BST
from ADTs.Queue_head import Queue
        
class SplayTree(BST):
    def splay(self, node):
        parent = node.parent
        print()
        print("node = %s"%node.key)
        if node == self.root:
            print("node is root")
            return
        #Node does NOT have a grandparent - ZIG
        elif parent == self.root:
            print('ZIG')
            if node.key > parent.key:
                print('node > parent')
                self.root = node
                parent.right = node.left
                node.left = parent
                node.parent = None
                parent.parent = node
                if parent.right != None:
                    parent.right.parent = parent
                return
            else:
                print('node < parent')
                self.root = node
                parent.left = node.right
                node.right = parent
                node.parent = None
                parent.parent = node
                if parent.left != None:
                    parent.left.parent = parent
                return
        #Node DOES have a grandparent
        else:
            print('node has gp')
            gparent = parent.parent
            if(node.key < parent.key and parent.key < gparent.key):
                print('ZIG-ZIG')
                print('BOTH LEFT')
                if gparent ==self.root:
                    self.root = node
                    node.parent = None
                else:
                    if gparent.key < gparent.parent.key:
                        gparent.parent.left = node
                    else:
                        gparent.parent.right = node
                    node.parent = gparent.parent
                parent.left = node.right
                if parent.left != None:
                    parent.left.parent = parent
                node.right = parent
                parent.parent = node
                gparent.left = parent.right
                if gparent.left != None:
                    gparent.left.parent = gparent
                parent.right = gparent
                
                gparent.parent = parent
            elif(node.key > parent.key and parent.key > parent.parent.key):
                print('ZIG-ZIG')
                print('BOTH RIGHT')
                if gparent ==self.root:
                    self.root = node
                    node.parent = None
                else:
                    if gparent.key < gparent.parent.key:
                        gparent.parent.left = node
                    else:
                        gparent.parent.right = node
                    node.parent = gparent.parent
                parent.right = node.left
                if parent.right != None:
                    parent.right.parent = parent
                node.left = parent
                parent.parent = node
                gparent.right = parent.left
                if gparent.right != None:
                    gparent.right.parent = gparent
                parent.left = gparent
                
                gparent.parent = parent
            else:
                print('ZIG-ZAG')
                if gparent == self.root:
                    self.root = node
                    node.parent = None
                else:
                    if gparent.key < gparent.parent.key:
                        gparent.parent.left= node
                    else:
                        gparent.parent.right = node
                    node.parent = gparent.parent
                if parent.key < gparent.key:
                    print('parent < gparent')
                    parent.right = node.left
                    if parent.right != None:
                        parent.right.parent = parent
                    node.left = parent
                    parent.parent = node
                    gparent.left = node.right
                    if gparent.left != None:
                        gparent.left.parent = gparent
                    node.right = gparent
                    
                    gparent.parent = node
                else:#parent > gparent
                    print('parent > gparent')
                    gparent.right = node.left
                    if gparent.right != None:
                        gparent.right.parent = gparent
                    node.left = gparent
                    gparent.parent = node
                    parent.left = node.right
                    if parent.left != None:
                        parent.left.parent = parent
                    node.right = parent
                    
                    parent.parent = node
            if self.root != node:
                print('node is not root')
                print('node = %s'%node.key)
                self.splay(node)
                return
            else:
                print('node is root')
                
    def insert(self, key, root=None):
        if(not self.root):
            self.root = Node(key,None,None,None)
            return True
        if(not root):
            root = self.root
        if(key == root.key):
            self.splay(root)
            return False
        elif(key > root.key):
            if(not root.right):
                root.right = Node(key,None,None,root)
                self.splay(root.right)
                return True
            newRoot = root.right
        else:
            if(not root.left):
                root.left = Node(key,None,None,root)
                self.splay(root.left)
                return True
            newRoot = root.left
        return self.insert(key, newRoot)
    
    def find(self, key, root=None):
        if(not root):
            if(not self.root):
                return False
            root = self.root
        if(key == root.key):
            self.splay(root)
            return True
        elif(key > root.key):
            if(not root.right):
                return False
            return self.find(key,root.right)
        else:
            if(not root.left):
                return False
            return self.find(key,root.left)
    
    def delete(self, key, root=None):
        #alternate between using inorder predecessor and successor
        if(not root):
            if(not self.root):
                return False
            root = self.root
        if(key == root.key):
            #If leaf node:
            if(not root.left and not root.right):
                #root node
                if(not root.parent):
                    self.root = None
                elif(root.parent.right == root):
                    root.parent.right = None
                else:
                    root.parent.left = None
                root = None
                return True
            #If only 1 child (right)
            elif(not root.left and root.right):
                #root node
                if(not root.parent):
                    self.root = root.right
                elif(root.parent.right == root):
                    root.parent.right = root.right
                else:
                    root.parent.left = root.right
                root.right.parent = root.parent
                root = None
                return True
            #If only 1 child (left)
            elif(root.left and not root.right):
                #root node
                if(not root.parent):
                    self.root = root.left
                if(root.parent.right == root):
                    root.parent.right = root.left
                else:
                    root.parent.left = root.left
                root.left.parent = root.parent
                root = None                    
                return True
            #If 2 children
            else:
                if(self.replaceWithSuccessor):
                    #Greatest Right Child (inorder successor)
                    childptr = root.right
                    while childptr.left:
                        childptr = childptr.left
                    root.key = childptr.key
                    #if replacement node has a right child
                    if(childptr.right):
                        if(childptr.parent.right == childptr):
                            childptr.parent.right = childptr.right
                        else:
                            childptr.parent.left = childptr.right
                        childptr.right.parent = childptr.parent
                    else:
                        if(childptr.parent.right == childptr):
                            childptr.parent.right = None
                        else:
                            childptr.parent.left = None
                    childptr = None
                else:
                    #Greatest Left Child (inorder predecessor)
                    childptr = root.left
                    while childptr.right:
                        childptr = childptr.right
                    root.key = childptr.key
                    #if replacement node has a left child
                    if(childptr.left):
                        if(childptr.parent.right == childptr):
                            childptr.parent.right = childptr.left
                        else:
                            childptr.parent.left = childptr.left
                        childptr.left.parent = childptr.parent
                    else:
                        if(childptr.parent.right == childptr):
                            childptr.parent.right = None
                        else:
                            childptr.parent.left = None
                    childptr = None
                self.replaceWithSuccessor = not self.replaceWithSuccessor
                return True
        elif(key > root.key):
            if(root.right):
                return self.delete(key, root.right)
        else:
            if(root.left):
                return self.delete(key,root.left)
        return False
    
    def traverseBFS(self):
        string = ''
        bfsQ = Queue()
        bfsQ.enQueue(self.root)
        cur = bfsQ.deQueue()
        while cur:
            string += ('\n(P%s)<-'%cur.parent.key if cur.parent else '(PNone)<-')
            string += str(cur.key)
            string += ('->(L%s'%cur.left.key if cur.left else '->(LNone')
            string += ('R%s)\n'%cur.right.key if cur.right else 'RNone)\n')
            if(cur.left):
                bfsQ.enQueue(cur.left)
            if(cur.right):
                bfsQ.enQueue(cur.right)
            cur = bfsQ.deQueue()
        return string
    
    def findRecentAccessed(self):
        return self.root.key
    
if __name__ == '__main__':
    st = SplayTree()
    
    for value in [10,15,5,6,9,7,12,1,3]:
        st.insert(value)
        
    st.find(7)
    
    print('--------------------')
    print(st)
    #print(st.findRecentAccessed())