class SquareIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        result = self.current ** 2
        self.current += 1
        return result

squares = SquareIterator(5)
for square in squares:
    print(square)