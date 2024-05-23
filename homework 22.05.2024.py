# class FibonacciIterator:
#     def __init__(self):
#         self.a = 0
#         self.b = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         item = self.a
#         self.a, self.b = self.b, self.a + self.b
#         return item
#
# fibonacci = FibonacciIterator()
# for i in fibonacci:
#     print(i)

# def fibonacci_generator():
#     a = 0
#     b = 1
#     while True:
#         yield a
#         a, b = b, a + b
#
# fibonacci_gen = fibonacci_generator()
# for i in fibonacci_gen:
#     print(i)


def programming_language():
    while True:
        yield "Java"
        yield "Python"
        yield "C++"
        yield "C#"
        yield "PHP"
        yield "JavaScript"
        yield "Ruby"
        yield "Scala"
        yield "Go"
        yield "Pascal"

pl = programming_language()

for i in pl:
    print(i)
    if i == "Go":
        pl.close()
    elif i == "Scala":
        pl.throw(Exception)