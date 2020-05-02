class Node:
	def __init__(self, key = None):
		self.key = key
		self.next = self.prev = self
class DoublyLinkedList:
	def __init__(self):
		self.head = Node(None)
		self.lenth = 0
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
		x.prev.next = x.next
		x.next.prev = x.prev
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
	def join(self,a):
		a.head.next.prev = self.head.prev
		a.head.prev.next = self.head
		self.head.prev.next = a.head.next
		self.head.prev = a.head.prev
	def split(self,a,b):
		Spl = DoublyLinkedList()
		a.prev.next, a.next.prev = a.next, a.prev
		b.prev.next, b.next.prev = b.next, b.prev
		Spl.head.next, Spl.head.prev = a, b
		return Spl
	
def josephus(n,k):
	L = DoublyLinkedList() # DoublyLinkedList 클래스 인스탠스 L을 선언
	for i in range(1,n+1):# 1번부터 n번까지의 key 값을 갖는 노드를 pushBack 함수를 써서 L에 삽입
		L.pushBack(i)
	x = L.head.next
	#for i in range(n-1): # 0~n-2 = n-1번 수행!
	while L.head.next.next != L.head:
		for j in range(k-1): # 0~k-2 : k-1번 수행!. k로 고치면 구름실습 정답.
			x = x.next
			xn = x.next
			if x == L.head:
				x = L.head.next
		xn = x.next
		if xn == L.head:
			xn = L.head.next
		L.deleteNode(x)
		x = xn
	return L.head.next.key

s = input().split()
n = int(s[0])
k = int(s[1])
res = josephus(n,k)
print(res)
