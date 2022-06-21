import math

class Shapes:
    
    def __init__(self, x=0, y=0, z=0, result=0):

        self.x = x
        self.y = y
        self.z = z
        self.result = result
        

class triangle(Shapes):
    def calculator(self):
        return float(self.x + self.y +self.z)/2
class circle(Shapes):
    def calculator(self):
	    return float(3.14159265*self.x*self.x)
class rectangle(Shapes):
    def calculator(self):
        return float(self.x * self.y)

while True:
    print("Find the area of \n 1. Triangle \n 2. Circle \n 3. Rectangle")
    shape = int(input("Type Here: "))

    if shape == 1:
        Side_A = int(input("Input Side A: "))
        Side_B = int(input("Input Side B: "))
        Side_C = int(input("Input Side C: "))
        triangle1 = triangle(Side_A,Side_B,Side_C)
        triangle2 = triangle1.calculator()
        result = triangle2
        result_2 = result*(result-Side_A)*(result-Side_B)*(result-Side_C)
        print("Area of triangle is: "+ str(float(math.sqrt(result_2))))

    if shape == 2:
        Radius = int(input("Input Radius: "))
        circle1 = circle(Radius)
        circle2 = circle1.calculator()
        result = circle2
        print("Area of Circle is: "+ str(float(result)))
    if shape == 3:
        length = int(input("Input length: "))
        width = int(input("Input width: "))
        rectangle1 = rectangle(length,width)
        rectangle2 = rectangle1.calculator()
        result = rectangle2
        print("Area of Rectangle is: "+ str(float(result)))
        
    check = input("Do you want to calculate again? Y or N: ")
    if check.upper() == "Y":
        continue
    elif check.upper() == "N":
        print("Bye...")
        break

