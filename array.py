class array:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def __getitem(self, index):  # 인덱스가 0보다 작거나 size보다 크면 에러 발생
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.data[index]

    def __setitem__(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        self.data[index] = value

    def __len__(self):
        return self.size

    def __str__(self):
        return str(self.data)
    
# 예제 사용법:
if __name__ == "__main__":
    arr = array(5)
    arr[0] = 10
    arr[1] = 20
    arr[2] = 30
    print(arr)  # 출력: [10, 20, 30, None, None]
    print(arr[1])  # 출력: 20
    print(len(arr))  # 출력: 5
    try:
        print(arr[5])  # 에러 발생
    except IndexError as e:
        print(e)  # 출력: 인덱스 범위 초과