# 1. class Node 선언 부분
class Node:
	def __init__(self, key = None):
		self.key = key
		self.next = self.prev = self
# 2. class DoublyLinkedList 선언부분
class DoublyLinkedList:
	def __init__(self):
		self.head = Node(None)
	def splice(self,a,b,x):
		if a == None or b == None or x == None :
			return
		ap = a.prev
		bn = b.next
		xn = x.next
		ap.next = bn
		bn.prev = ap
		x.next = a
		a.prev = x
		xn.prev = b
		b.next = xn
	def moveAfter(self,a,x):
		self.splice(a,a,x)
	def moveBefore(self,a,x):
		self.splice(a,a,x.prev)
	def insertAfter(self,x,key):
		self.moveAfter(Node(key),x)
	def insertBefore(self,x,key):
		self.moveBefore(Node(key),x)
	def pushFront(self,key):
		self.insertAfter(self.head,key)
	def pushBack(self,key):
		self.insertBefore(self.head,key)
	def printList(self):
		print("h -> ", end= "")
		v = self.head.next
		while v != self.head:
			print(str(v.key)+" -> ", end = "")
			v = v.next
		print("h")
	def search(self,key):
		v = self.head.next
		while v != self.head:
			if v.key == key : return v
			v = v.next
		return None
	def __iter__(self):
		v = self.head.next
		while v != self.head:
			yield v
			v = v.next
	def deleteNode(self,x):
		if x == None : return
		x.prev.next, x.next.prev = x.next, x.prev
		del x
	def isEmpty(self):
		if self.head == self.head.next:
			return 1
		else :
			return 0
	def popFront(self):
		if self.isEmpty() : return None
		key = self.head.next.key
		self.deleteNode(self.head.next)
		return key
	def popBack(self):
		if self.isEmpty() : return None
		key = self.head.prev.key
		self.deleteNode(self.head.prev)
		return key
	def first(self):
		return self.head.next.key
	def last(self):
		return self.head.prev.key
	def join(self, a):
		a.head.next.prev = self.head.prev
		a.head.prev.next = self.head
		self.head.prev.next = a.head.next
		self.head.prev = a.head.prev
	def split(self, a,b):
		Spl = DoublyLinkedList()
		a.prev.next, a.next.prev = a.next, a.prev
		b.prev.next, b.next.prev = b.next, b.prev
		Spl.head.next, Spl.head.prev = a, b
		return Spl
	
L = DoublyLinkedList()
while True:
    cmd = input().split()
    if cmd[0] == 'pushF':
        L.pushFront(int(cmd[1]))
        print("+ {0} is pushed at Front".format(cmd[1]))
    elif cmd[0] == 'pushB':
        L.pushBack(int(cmd[1]))
        print("+ {0} is pushed at Back".format(cmd[1]))
    elif cmd[0] == 'popF':
        key = L.popFront()
        if key == None:
            print("* list is empty")
        else:
            print("- {0} is popped from Front".format(key))
    elif cmd[0] == 'popB':
        key = L.popBack()
        if key == None:
            print("* list is empty")
        else:
            print("- {0} is popped from Back".format(key))
    elif cmd[0] == 'search':
        v = L.search(int(cmd[1]))
        if v == None: print("* {0} is not found!".format(cmd[1]))
        else: print(" * {0} is found!".format(cmd[1]))
    elif cmd[0] == 'insertA':
        # inserta key_x key : key의 새 노드를 key_x를 갖는 노드 뒤에 삽입
        x = L.search(int(cmd[1]))
        if x == None: print("* target node of key {0} doesn't exit".format(cmd[1]))
        else:
            L.insertAfter(x, int(cmd[2]))
            print("+ {0} is inserted After {1}".format(cmd[2], cmd[1]))
    elif cmd[0] == 'insertB':
        # inserta key_x key : key의 새 노드를 key_x를 갖는 노드 앞에 삽입
        x = L.search(int(cmd[1]))
        if x == None: print("* target node of key {0} doesn't exit".format(cmd[1]))
        else:
            L.insertBefore(x, int(cmd[2]))
            print("+ {0} is inserted Before {1}".format(cmd[2], cmd[1]))
    elif cmd[0] == 'delete':
        x = L.search(int(cmd[1]))
        if x == None:
            print("- {0} is not found, so nothing happens".format(cmd[1]))
        else:
            L.deleteNode(x)
            print("- {0} is deleted".format(cmd[1]))
    elif cmd[0] == "first":
        print("* {0} is the value at the front".format(L.first()))
    elif cmd[0] == "last":
        print("* {0} is the value at the back".format(L.last()))
    elif cmd[0] == 'print':
        L.printList()
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")
