class stack():
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):  # 스택이 비어있지 않으면 마지막 요소를 제거하고 반환, 비어있으면 에러 발생
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
    
# 예제 사용법:
if __name__ == "__main__":
    s = stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.peek())  # 출력: 3
    print(s.pop())   # 출력: 3
    print(s.size())  # 출력: 2
    print(s.is_empty())  # 출력: False
    s.pop()
    s.pop()
    print(s.is_empty())  # 출력: True