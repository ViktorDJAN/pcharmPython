# n = 4
# i=1
# b = 1
# while i <=n:
#     b = b*i
#     i+=1
# print(b)

# последовательность фибоначи

first = 0
second = 1
next = first + second
number = 21
while next <= number:
    first = second
    second = next
    next = first + second
    print(next)