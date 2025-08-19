#write a program to print the multiplication of user input table

n = int(input("Enter The table which you want to make: "))
print('multiplication of the table is: ')

for i in range(1,11):
    print(f'{n} X {i} = {n*i}')