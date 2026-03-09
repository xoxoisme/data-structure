class queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)
    
# 예제 사용법:
if __name__ == "__main__":
    q = queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.peek())  # 출력: 1
    print(q.dequeue())  # 출력: 1
    print(q.size())  # 출력: 2
    print(q.isEmpty())  # 출력: False
    q.dequeue()
    q.dequeue()
    print(q.isEmpty())  # 출력: True
    q.enqueue(4)
    print(q.peek())  # 출력: 4
    print(q.dequeue())  # 출력: 4
    print(q.isEmpty())  # 출력: True