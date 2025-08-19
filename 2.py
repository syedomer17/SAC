#write a program to check that the give number is prime or not
n = int(input("Enter the number:"))
count = 0
for i in range(1,n+1):
    if n % i == 0:
        count = count + 1
    
if count == 2:
    print(f'{n} is a prime number')
else:
    print(f'{n} is not a prime number')