class Node:
    def __init__(self, sz):
        self.array = [0] * sz
        self.next = None

class Queue:
    def __init__(self, limit):
        self.head = Node(limit)
        self.rear = self.head
        self.rear_pos = 0
        self.head_pos = 0
        self.limit = limit
        self.sz = 0

    def enqueue(self, item):
        self.rear.array[self.rear_pos] = item
        self.rear_pos += 1
        self.sz += 1
        if self.rear_pos == self.limit:
            self.rear.next = Node(self.limit)
            self.rear = self.rear.next
            self.rear_pos = 0

    def dequeue(self):
        if self.rear is self.head and self.head_pos == self.rear_pos:
            raise Exception('empty queue.')
        ret = self.head.array[self.head_pos]
        self.head_pos += 1
        self.sz -= 1
        if self.head_pos == self.limit:
            self.head = self.head.next
            self.head_pos = 0
        return ret

    def size(self):
        return self.sz

q = Queue(2)
for i in range(4): q.enqueue(i)
while q.size() > 0:
    print q.dequeue()

print q.dequeue()

