class Node:
    def __init__(self, v=None):
        self.__key = v
        self.__prev = self
        self.__next = self
    def getPrev(self):
        return self.__prev
    def setPrev(self, p):
        self.__prev = p
    def getNext(self):
        return self.__next
    def setNext(self, n):
        self.__next = n
    def getKey(self):
        return self.__key
    def setKey(self, v):
        self.__key = v
class CLL: # a circular Doubly Linked List
    def __init__(self):
        self.root = Node()
        self.root.setPrev(self.root)
        self.root.setNext(self.root)
    def splice(self, a, b, x):
        if a==None or b==None or x==None:
            return
        ap , bn = a.getPrev(), b.getNext()
        ap.setNext(bn)
        bn.setPrev(ap)
        xn = x.getNext()
        a.setPrev(x)
        x.setNext(a)
        b.setNext(xn)
        xn.setPrev(b)
    def moveAfter(self, a, x):
        self.splice(a,a,x)
    def moveBefore(self, a, x):
        self.splice(a,a,x.getPrev())
    def insertAfter(self, x, key):
        self.moveAfter(Node(key), x)
    def insertBefore(self, x, key):
        self.moveBefore(Node(key), x)
    def pushFront(self, key):
        self.insertAfter(self.root, key)
    def pushBack(self, key):
        self.insertBefore(self.root, key)
    def isEmpty(self):
        if self.root == self.root.getNext():
            return 1
        else:
            return 0
    def __len__(self):
        L = 0
        for _ in self:
            L += 1
        return L
    def __iter__(self):
        v = self.root.getNext()
        while v != self.root:
            yield v
            v = v.getNext()
    def delNode(self, x):
        if x == None: return
        xp, xn = x.getPrev(), x.getNext()
        xp.setNext(xn)
        xn.setPrev(xp)
        del x
    def popFront(self):
        if self.isEmpty():return -1
        key = self.root.getNext().getKey()
        self.delNode(self.root.getNext())
        return key
    def popBack(self):
        if self.isEmpty():return -1
        key = self.root.getPrev().getKey()
        self.delNode(self.root.getPrev())
        return key
    def front(self):
        if self.isEmpty():
            return -1
        return self.root.getNext().getKey()
    def back(self):
        if self.isEmpty():
            return -1
        return self.root.getPrev().getKey()
    def dragLeft(self):
        self.moveAfter(self.root, self.root.getNext())
    def dragRight(self):
        self.moveBefore(self.root, self.root.getPrev())
        
class deque:
    def __init__(self):
        self.CLL = CLL()
    def pushFront(self,x):
        self.CLL.pushFront(x)
    def pushBack(self, x):
        self.CLL.pushBack(x)
    def popFront(self):
        return self.CLL.popFront()
    def popBack(self):
        return self.CLL.popBack()
    def size(self):
        return len(self.CLL)
    def isEmpty(self):
        return self.CLL.isEmpty()
    def front(self):
        return self.CLL.front()
    def back(self):
        return self.CLL.back()
    def findR(self, key):
        count = 0
        first = self.front
        while self.front() != key:
            count += 1
            self.CLL.dragLeft()
            if self.front() == first:
                return -1
        self.popFront()
        return count
    def findL(self, key):
        count = 0
        first = self.front()
        while self.front() != key:
            count += 1
            self.CLL.dragRight()
            if self.front == first:
                return -1
        self.popFront()
        return count
    
import sys
input = sys.stdin.readline
n, c = map(int, input().split())
X = list(map(int, input().split()))
resL = 0
resR = 0
D = deque()
for i in range(1,n+1):
    D.pushBack(i)
for i in range(c):
    length = D.size()
    r  = D.findR(X[i])
    
    l = length - r
    if r != -1:
        if r > l:
            resL += l
        else :
            resR += r
print(resL + resR)
