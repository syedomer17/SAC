#write a program to program to print the fiboncci series from 0 to n by using reisive function

def f(n):
    if n == 0 or n == 1:
        return n
    else:
        return f(n - 1) + f(n - 2)

n = int(input('Enter the value of n: '))
print('Fibonacci series:')

for i in range(0, n + 1):
    print(f(i))
