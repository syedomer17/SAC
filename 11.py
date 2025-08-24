#write a program to calculate the area and perimert  of a rectangle by using class and object

class rectangle:
    def read(self): 
        self.l = int(input('Enter length of rectangle:'))
        self.b = int(input('Enter the breath of rectangle:'))

    def area(self): 
        self.a = self.l * self.b 
    
    def perimeter(self): 
        self.p = 2*(self.l + self.b)
    
    def display(self): 
        self.area()
        self.perimeter()
        print(f'area of rectangle:{self.a}')
        print(f'perimeter of rectangle:{self.p}')


r = rectangle()
r.read()
r.display()