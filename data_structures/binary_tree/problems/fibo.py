from time import time


def fib(n):
    if n == 0:
        print('Error')
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


fib_arr = [0, 1]


def fib2(n):
    if n == 0:
        print("Error")
    elif n <= len(fib_arr):
        return fib_arr[n-1]
    else:
        temp = fib2(n-1) + fib2(n-2)
        fib_arr.append(temp)
        return temp


def print_fib(n):
    fib = [0, 1]
    print(0)
    print(1)
    for i in range(1, n):
        print(fib[i] + fib[i-1])
        fib.append(fib[i] + fib[i-1])

    print(fib)

# start = time()
# print(fib(35))
# end = time()
# print(end-start)
#
# print("-----------------")

start = time()
x = fib2(999)
print(x)
end = time()
print(end-start)

print("%.100f" % float(end-start))
# print(round(end2-start2))
# 0, 1, 1, 2 ,3. 5, 8, 13, 21

print_fib(8)