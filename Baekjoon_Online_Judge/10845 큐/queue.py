import sys
class Queue:
    def __init__(self):
        self.items = []
        self.head = 0
        self.tail = -1
    def push(self, x):
        self.items.append(x)
        self.tail += 1
    def pop(self):
        if len(self) <= 0:
            return -1
        i = self.head
        self.head += 1
        return self.items[i]
    def __len__(self):
        return self.tail - self.head + 1
    def isEmpty(self):
        return 1 if len(self)==0 else 0
    def front(self):
        return self.items[self.head] if len(self) else -1
    def back(self):
        return self.items[self.tail] if len(self) else -1

input = sys.stdin.readline
n = int(input())
Q = Queue()
for i in range(n):
    comm = input().split()
    if comm[0] == "push":
        Q.push(int(comm[1]))
    elif comm[0] == "pop":
        print(Q.pop())
    elif comm[0] == "size":
        print(len(Q))
    elif comm[0] == "empty":
        print(Q.isEmpty())
    elif comm[0] == "front":
        print(Q.front())
    elif comm[0] == "back":
        print(Q.back())
