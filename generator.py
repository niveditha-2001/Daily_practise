# # 1. Write a generator function that produces the Fibonacci sequence indefinitely. Use yield to return the next number in the sequence.
# n=int(input('enter the number'))
# a=0
# b=1
# if n<0:
#     return 0
# else:
#     for i in range(0,n):
#         yield a
#         c=a+b
#         b=a-c
#         a=b-c


# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
# fib_gen = fibonacci()
# for i in range(0,10):
#     print(next(fib_gen))

# Write a generator that calculates the running sum of numbers sent to it using send. If None is sent, it should return the current total.
# def numberGenerator(n):
#     number = yield
#     #print(number)
#     while number < n:
#         number = yield number
#         #print(number)
#         number += 1
# g = numberGenerator(10)
# g.send(None)
# print(g.send(5))
# print(g.send(6))
# print(g.send(5))

# Implement a class-based iterator to generate the first n prime numbers.
