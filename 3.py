#write a program to store n elements in a array list and print those elements
n = int(input('Enter the number of elements:'))
a = []
print(f'Enter {n} elements:')
for i in range(0,n):
    x = int(input())
    a.append(x)

print(f'Input list: {a}')
