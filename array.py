class array:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def __getitem__(self, index):
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
# Example usage:
if __name__ == "__main__":
    arr = array(5)
    arr[0] = 10
    arr[1] = 20
    arr[2] = 30
    print(arr)  # Output: [10, 20, 30, None, None]
    print(arr[1])  # Output: 20
    print(len(arr))  # Output: 5
    try:
        print(arr[5])  # This will raise an IndexError
    except IndexError as e:
        print(e)  # Output: Index out of bounds