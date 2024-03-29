#WAP to demonstrate the use of method overriding.

# Parent class
class Shape:
    # properties
    data1 = "abc"

    # function no_of_sides
    def no_of_sides(self):
        print("My sides need to be defined. I am from shape class.")

    # function two_dimensional
    def two_dimensional(self):
        print("I am a 2D object. I am from shape class")

#Sub-class
class Square(Shape):
    data2 = "xyz"

    def no_of_sides(self):
        print("I have 4 sides. I am from Square class")

    def color(self):
        print("I have teal color. I am from Square class.")


# Create an object of Square class
sq = Square()
# Override the no_of_sides of parent class
sq.no_of_sides()
# Will inherit this method from the parent class
sq.two_dimensional()
# It's own method - color
sq.color()
print("Old value of data1 = ", sq.data1)
# Override property of the Parent class
sq.data1 = "New value"
print("The value of data1 in Shape class overridden by the Square class = ", sq.data1)
