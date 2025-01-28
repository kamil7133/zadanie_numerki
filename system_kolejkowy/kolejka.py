class Kolejka:
    def __init__(self):
        self.elementy = []

    def enqueue(self, item):
        self.elementy.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.elementy.pop(0)

    def front(self):
        if self.is_empty():
            return None
        return self.elementy[0]

    def is_empty(self):
        return len(self.elementy) == 0

    def size(self):
        return len(self.elementy)
