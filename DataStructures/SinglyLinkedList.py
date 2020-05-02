class Node:
    def __init__(self, key = None, value  = None):
        self.key = key
        self.value = value
        self.next = None
    def __str__(self):
        return str(self.key)

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    def __iter__(self):
        v = self.head
        while v != None:
            yield v
            v = v.next
    def __str__(self):
        return " -> ".join(str(v) for v in self)
    def pushFront(self, key, value = None):
        newNode = Node(key, value)
        newNode.next = self.head
        self.head = newNode
        self.size += 1
    def pushBack(self, key, value = None):
        newNode = Node(key, value)
        if self.size == 0 :
            self.head = newNode
        else :
            tail = self.head
            while tail.next != None:
                tail = tail.next
            tail.next = newNode
        self.size += 1
    def popFront(self):
        if self.size == 0 : return None
        else :
            h = self.head
            key = h.key
            self.head = self.head.next
            del h
            self.size -= 1
            return key
    def popBack(self):
        if self.size == 0: return None
        else : 
            tail = self.head
            prev = None
            while tail.next != None:
                prev = tail
                tail = tail.next
            prev.next = None
            key = tail.key
            del tail
            self.size -= 1
            return key
    def search(self, key):
        v = self.head
        while v != None:
            if v.key == key: return v
            v = v.next
        return h
    def remove(self, key):
        if self.size == 0 or key ==  None :
            return
        elif self.head.key == key:
            self.popFront()
        else :
            v = self.head
            prev = None
            while v.key != key :
                prev = v
                v = v.next
            prev.next = v.next
            del v
            self.size -=1
    def __len__(self):
        count = 0
        v = self.head 
        while v != None :
            count += 1
            v = v.next
        return count
