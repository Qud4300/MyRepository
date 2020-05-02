# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None
    def __str__(self):
        return str(self.key)
    
class Tree:
    def __init__(self):
        self.root = None
        self.size = 0
    def __len__(self):
        return self.size
    def preorder(self, v):
        if v != None:
            print(v.key, end=' ')
            self.preorder(v.left)
            self.preorder(v.right)
    def inorder(self, v):
        if v != None:
            self.inorder(v.left)
            print(v.key, end=' ')
            self.inorder(v.right)
    def postorder(self, v):
        if v != None:
            self.postorder(v.left)
            self.postorder(v.right)
            print(v.key, end=' ')
    def find_loc(self, key):
        if self.size == 0:
            return None
        p = None
        v = self.root
        while v:
            if v.key == key:
                return v
            elif v.key < key:
                p = v
                v = v.right
            else:
                p = v
                v = v.left
        return p
    def search(self, key):
        p = self.find_loc(key)
        if p and p.key == key:
            return p
        else:
            return None
    def insert(self, key):
        v = None
        p = self.find_loc(key)
        if p == None:
            v = self.root= Node(key)
        elif p.key != key:
            v = Node(key)
            v.parent = p
            if p.key > key:
                p.left = v
            else:
                p.right = v
        self.size = self.size + 1
        return v
    
class SplayTree(Tree):
    def right_rotate(self, x):
        a, p = x.left, x.parent
        #x-aR
        x.left = a.right
        if a.right:
            a.right.parent = x
        #p-a
        a.parent = p
        if p:#p isnt None
            if p.left == x:
                p.left = a
            else:
                p.right = a
        else:#p == none
            self.root = a
        #a-x
        a.right = x
        x.parent = a
        return x.parent
    def left_rotate(self, x):
        a, p = x.right, x.parent
        #x-aL
        x.right = a.left
        if a.left:
            a.left.parent = x
        #p-a
        a.parent = p
        if p:
            if p.left == x:
                p.left = a
            else:
                p.right = a
        else:#p == none
            self.root = a
        #a-x
        a.left = x
        x.parent = a
        return x.parent
    def splay(self, a):
        while a.parent:
            if a.parent.left == a:
                a = self.right_rotate(a.parent)
            else:
                a = self.left_rotate(a.parent)
        return self.root
    def search(self, key):
        v = super(SplayTree, self).search(key)
        if v :
            self.root = self.splay(v)
            return self.root
        return None
    def insert(self, key):
        v = super(SplayTree, self).insert(key)
        v = self.splay(v)
        return v
    def delete(self, x):
        self.splay(x)
        L, R = x.left, x.right
        if L :
            m = L
            while m.right: m = m.right
            m = self.splay(m) # m is root!
            m.right = R
            if R:
                R.parent = m
        elif R : #L is None, R exist
            R.parent = None
            self.root = R
        else : # L,R nothing exist
            self.root = None
    def preorder(self, v):
        super(SplayTree, self).preorder(v)
    def postorder(self, v):
        super(SplayTree, self).postorder(v)
    def inorder(self, v):
        super(SplayTree, self).inorder(v)
T = SplayTree()
while True:
    cmd = input().split()
    if cmd[0] == 'in':
        v = T.insert(int(cmd[1]))
        print("+ {0} is inserted".format(v.key))
    elif cmd[0] == 'del':
        v = T.search(int(cmd[1]))
        T.delete(v)
        print("- {0} is deleted".format(int(cmd[1])))
    elif cmd[0] == 'find':
        v = T.search(int(cmd[1]))
        if v == None: print("* {0} is not found!".format(cmd[1]))
        else: print(" * {0} is found!".format(cmd[1]))
    elif cmd[0] == 'preorder':
        T.preorder(T.root)
        print()
    elif cmd[0] == 'postorder':
        T.postorder(T.root)
        print()
    elif cmd[0] == 'inorder':
        T.inorder(T.root)
        print()
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")
