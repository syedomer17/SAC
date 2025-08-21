#write a program to find sum of elements max element and min elements of the list

n = int(input('Enter the number of elements: '))
a = []
print(f'Enter {n} elemennts of the list: ')
sum = 0

for i in range(0,n):
    x = int(input())
    a.append(x)

    sum = sum + a[i]

    if i == 0:
        max = a[0]
        min = a[0]
    else:
        if a[i] > max:
            max = a[i]
        if a[i] < min:
            min = a[i]

print(f'input list: {a}')
print(f'sum of the elements:{sum}')
print(f'max value: {max}')
print(f'min value: {min}')