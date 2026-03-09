class doubly_linked_list:
    class node:
        def __init__(self, data):
            self.data = data
            self.prev = None
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head is None
    
    def append(self, data):
        new_node = self.node(data)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = self.node(data)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next is not None:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return
            current = current.next
            
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next
        print()

# 예제 사용법:
if __name__ == "__main__":
    dll = doubly_linked_list()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.display()  # 출력: 1 2 3
    dll.prepend(0)
    dll.display()  # 출력: 0 1 2 3
    dll.delete(2)
    dll.display()  # 출력: 0 1 3
    print(dll.isEmpty())  # 출력: False
    dll.delete(0)
    dll.delete(1)
    dll.delete(3)
    print(dll.isEmpty())  # 출력: True