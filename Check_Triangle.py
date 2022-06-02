"""
This method return the type of the triangle Equilateral, Isosceles or Scalene
Params a,b,c are an integers and is a side of the triangle
Return the type of the triangle
"""
def get_triangle_type(a,b,c):
    if(a == b and b == c and c == a):
        print("The Triangle is Equilateral")
    elif(a == b or b == c or c == a):
        print("The Triangle is Isosceles")
    else:
        print("The Triangle is Scalene")

"""
This method check if is posible to create a triangle
@Param sides, is a list of integers that have the sides of the triangle
@Return if is posible to create a triangle and if it is posible call other method that return the type of the triangle
"""
def check_triangle(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    print_sides_of_tringle(a,b,c)
    if(a + b > c and b + c > a and a + c > b):
        get_triangle_type(a,b,c)
    else:
        print("Error to get the type of the triangle because is not posible to build a triangle with that sides")

def print_sides_of_tringle(a,b,c):
    print(a)
    print(b)
    print(c)

# Principal Method that execute all the logic of the program
def main():
    sides = [4,4,4]
    check_triangle(sides)

if __name__ == "__main__":
    main()