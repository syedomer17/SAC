#write a program to display fibnoccci serice from 0 to n by using arrray list

n = int(input('Enter the number:'))
f = []
f.append(0)
f.append(1)

for i in range(2,n+1):
    f.append(f[i-1] + f[i-2])

print(f'fibonacci series:{f}')