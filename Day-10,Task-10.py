class Counter:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    # Iterator returns itself
    def __iter__(self):
        return self

    # Returns next value or raises StopIteration
    def __next__(self):
        if self.current <= self.end:
            val = self.current
            self.current += 1
            return val
        else:
            raise StopIteration


# Using Counter in a loop
for i in Counter(1, 5):
    print(i)
