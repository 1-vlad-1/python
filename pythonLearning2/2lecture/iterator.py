class Fib:
    '''Итератор, который возвращает числа в последовательности Фибоначчи'''

    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib

iter = Fib(100)

for i in iter:
    print(i)


def Gen(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b
        
print(list(Gen(5)))