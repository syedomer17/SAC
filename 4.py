#write a program to check give key element belongs to the list or not

x = int(input("Enter the number:"))
a = []
print(f'Entered {x} elements:')
for i in range(0,x):
    n = int(input())
    a.append(x)

print(f'Input list:{a}')
key = int(input('Enter the key element to search:'))
if key in a:
    print(f'{key} foundin {a}')
else:
    print(f'{key} not found in {a}')