#write a program to sort the elements of theb list ascending order or descending or order

n = int(input('Enter the number:'))
a = []
print(f'Enter {n} elements:')

for i in range(0,n):
    x = int(input())
    a.append(x)

print(f'Input list {a}')
a.sort()
print(f'list in aesending order:{a}')

a.sort(reverse=True)
print(f'list in desending order:{a}')