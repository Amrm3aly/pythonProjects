import math
############## FUNCTIONS ###############
def get_shape(shape) :
    shape = shape.lower()
    if shape == "circle" :
        circle_area() 
    elif shape == "rectangle" :
        rectangle_area()
    elif shape == "square" :
        square_area()
    elif shape == "triangle":
        triangle_area() 
    elif shape == "parallelo gram":
        paralleloGram_area()
    elif shape == "trapezium":
        trapezium_area()
    elif shape == "ellipse":
        ellipse_area()         
    else :
        print("working on it !!")

######### Calculate circle area ##############
def circle_area() :
    radious=float(input("enter the radious value for the circle : "))
    area = math.pi * pow(radious , 2) 
    print(f"the area of the circle = {area}")

######### Calculate rectangle area ##########
def rectangle_area() :
    length = float(input("Enter the Length value of the rectangle : "))
    width = float(input("Enter the width value of the rectangle : "))
    area = length * width 
    print(f"the area of the rectangle = {area}")

######## Calculate square area #########
def square_area() :
    Length=float(input("Enter the Length value of the side : "))   
    area=pow(Length ,2 )
    print(f"The Area of the square = {area}")

######## Calculate Triangle area #######
def triangle_area() :
    base = float(input("Enter the base value : "))
    height = float(input("Enter the height value : "))
    area = 0.5 * base * height
    print(f"The area of the Triangle = {area}")

######## Calculate parallelo gram area #######
def paralleloGram_area() : 
    base = float(input("Enter the base value : "))
    height = float(input("Enter the vertical height value : "))
    area= base * height
    print(f"The area of the parallelo gram = {area}")
######## Calculate Trapezium  area #######
def trapezium_area():
    side1=float(input("Enter the length value for the first side : "))
    side2=float(input("Enter the length value for the second side : "))
    height=float(input("Enter the height value : "))
    area= 0.5*(side1 + side2)*height
    print(f"the area of the trapezium = {area}") 

######## calculate ellipse area ########
def ellipse_area() :
    minor=float(input("Enter the minor axis value : "))
    major=float(input("Enter the major axis value : "))      
    minor = minor *0.5
    major = major*0.5
    area= math.pi * minor * major 
    print(f"The area of the ellipse = {area}")
        

shape_type = input("which shape you want to calc its area : ")
get_shape(shape_type)
