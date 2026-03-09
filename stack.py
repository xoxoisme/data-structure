class stack():
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty")
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Stack is empty")
    def is_empty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)
# Example usage:
if __name__ == "__main__":
    s = stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.peek())  # Output: 3
    print(s.pop())   # Output: 3
    print(s.size())  # Output: 2
    print(s.is_empty())  # Output: False
    s.pop()
    s.pop()
    print(s.is_empty())  # Output: True