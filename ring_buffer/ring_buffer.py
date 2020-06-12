class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * self.capacity
        self.pointer = 0

    def append(self, item):
        self.storage[self.pointer] = item
        self.pointer = (self.pointer + 1) % self.capacity
        print(self.pointer)

    def get(self):
        return [item for item in self.storage if item is not None]


test_buffer = RingBuffer(5)
test_buffer.append(1)
test_buffer.append(2)

print(test_buffer.storage)
print(test_buffer.get())
