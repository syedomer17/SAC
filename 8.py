#write a program to print fibonacci series from 0,1 by using non reisive function

def f(n):
    t1 = 0
    t2 = 1
    print(t1,end=" ")
    print(t2,end=" ")
    for i in range(2,n+1):
        t3 = t1 + t2
        print(t3,end=" ")
        t1 =  t2
        t2 = t3

n = int(input('Enter the value of n: '))
print('fibonocci series:')
f(n)