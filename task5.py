class Buffer:
    def __init__(self):
        self.storage = []

    def add(self, *a: int):
        self.storage.extend(a)
        print(f"Буфер до: {self.get_current_part()}")

        while len(self.storage) >= 5:
            currentFive = self.storage[:5]
            print(f"Сума з 5 елементів: {sum(currentFive)}")
            self.storage = self.storage[5:]

    def get_current_part(self):
        return self.storage


buffer = Buffer()
buffer.add(1, 2, 3)
print(f"Буфер після: {buffer.get_current_part()}")
buffer.add(4, 5, 6)
print(f"Буфер після: {buffer.get_current_part()}")
buffer.add(7, 8, 9, 10)
print(f"Буфер після: {buffer.get_current_part()}")
buffer.add(11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22)
print(f"Буфер після: {buffer.get_current_part()}")