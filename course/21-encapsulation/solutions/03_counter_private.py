"""Solution — Exercise 3: A counter with a hidden count."""

class Counter:
    def __init__(self):
        self.__count = 0

    def increment(self):
        self.__count += 1

    def value(self):
        return self.__count

c = Counter()
c.increment()
c.increment()
c.increment()
print(c.value())
