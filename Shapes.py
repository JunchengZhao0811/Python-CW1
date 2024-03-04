from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def getArea(self):
        pass

    @abstractmethod
    def getVolume(self):
        pass

class Point(Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getName(self):
        return "Point"

    def toString(self):
        return "[" + str(self.x) + "," + str(self.y) + "]"

    def getArea(self):
        return 0

    def getVolume(self):
        return 0

class Circle(Point):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.__r = 0
        self.radius = r

    def getName(self):
        return "Circle"

    def getArea(self):
        return math.pi * self.__r ** 2

    def toString(self):
        return f"C = {super().toString()}; R = {self.__r}"

    @property
    def radius(self):
        return self.__r

    @radius.setter
    def radius(self, r):
        if r > 0:
            self.__r = r
        else:
            print("Radius must be positive.")

class Cylinder(Circle):
    def __init__(self, x, y, r, h):
        super().__init__(x, y, r)
        self.__h = 0
        self.height = h

    def getName(self):
        return "Cylinder"

    def getArea(self):
        return 2 * super().getArea() + 2 * math.pi * self.radius * self.__h

    def getVolume(self):
        return super().getArea() * self.__h

    def toString(self):
        return f"{super().toString()}; H = {self.__h}"

    @property
    def height(self):
        return self.__h

    @height.setter
    def height(self, h):
        if h > 0:
            self.__h = h
        else:
            print("Height must be positive.")

class Sphere(Circle):
    def __init__(self, x, y, r):
        super().__init__(x, y, r)

    def getName(self):
        return "Sphere"

    def getArea(self):
        return 4 * math.pi * self.radius ** 2

    def getVolume(self):
        return (4/3) * math.pi * self.radius ** 3

    def toString(self):
        return f"{super().toString()}"

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def getName(self):
        return "Rectangle"

    def getArea(self):
        return self.length * self.width

    def getVolume(self):
        return 0

    def toString(self):
        return f"L = {self.length}; W = {self.width}"

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.__side = side

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        self.__side = value
        self.length = self.width = value

    def getName(self):
        return "Square"

    def getArea(self):
        return self.side ** 2

    def getVolume(self):
        return 0

    def toString(self):
        return f"A = {self.side}"

class Cube(Square):
    def __init__(self, side):
        super().__init__(side)

    def getName(self):
        return "Cube"

    def getArea(self):
        return 6 * self.side ** 2

    def getVolume(self):
        return self.side ** 3

    def toString(self):
        return f"A = {self.side}"

def get_positive_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Value must be positive. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_point_parameters():
    x = get_positive_input("Enter x coordinate: ")
    y = get_positive_input("Enter y coordinate: ")
    return x, y

def get_circle_parameters():
    x, y = get_point_parameters()
    r = get_positive_input("Enter radius: ")
    return x, y, r

def get_rectangle_parameters():
    length = get_positive_input("Enter length: ")
    width = get_positive_input("Enter width: ")
    return length, width

def get_square_parameters():
    side = get_positive_input("Enter side length: ")
    return side

def get_cylinder_parameters():
    x, y, r = get_circle_parameters()
    h = get_positive_input("Enter height: ")
    return x, y, r, h

def get_cube_parameters():
    side = get_positive_input("Enter side length: ")
    return side

def create_shape():
    shape_type = input("Enter shape type (Point, Circle, Rectangle, Square, Sphere, Cylinder, Cube): ").lower()  # Convert input to lowercase
    if shape_type == "point":
        x, y = get_point_parameters()
        return Point(x, y)
    elif shape_type == "circle":
        x, y, r = get_circle_parameters()
        return Circle(x, y, r)
    elif shape_type == "rectangle":
        length, width = get_rectangle_parameters()
        return Rectangle(length, width)
    elif shape_type == "square":
        side = get_square_parameters()
        return Square(side)
    elif shape_type == "sphere":
        x, y, r = get_circle_parameters()
        return Sphere(x, y, r)
    elif shape_type == "cylinder":
        x, y, r, h = get_cylinder_parameters()
        return Cylinder(x, y, r, h)
    elif shape_type == "cube":
        side = get_cube_parameters()
        return Cube(side)
    else:
        print("Shape type not recognized.")
        return None

def list_shapes(shapes):
    if not shapes:
        print("No shapes to display.")
    else:
        for i, shape in enumerate(shapes, start=1):
            print(f"{i}: {shape.getName()} ({shape.toString()})")
        print("Shapes listed successfully.")

def modify_shape(shapes):
    if not shapes:
        print("No shapes available to modify.")
        return

    list_shapes(shapes)
    index = int(input("Enter the index of the shape to modify: ")) - 1
    if index < 0 or index >= len(shapes):
        print("Invalid index.")
        return

    shape = shapes[index]
    print(f"Modifying {shape.getName()}...")

    if isinstance(shape, Point) and not isinstance(shape, Circle):
        x, y = get_point_parameters()
        shape.x = x
        shape.y = y
    elif isinstance(shape, Circle) and not isinstance(shape, Cylinder) and not isinstance(shape, Sphere):
        x, y, r = get_circle_parameters()
        shape.x = x
        shape.y = y
        shape.radius = r
    elif isinstance(shape, Cylinder):
        x, y, r, h = get_cylinder_parameters()
        shape.x = x
        shape.y = y
        shape.radius = r
        shape.height = h
    elif isinstance(shape, Sphere):
        x, y, r = get_circle_parameters()
        shape.x = x
        shape.y = y
        shape.radius = r
    elif isinstance(shape, Rectangle) and not isinstance(shape, Square):
        length, width = get_rectangle_parameters()
        shape.length = length
        shape.width = width
    elif isinstance(shape, Square) or isinstance(shape, Cube):
        side = get_square_parameters()
        shape.side = side
    print("Shape modified successfully.")

def delete_shape(shapes):
    if not shapes:
        print("No shapes to delete.")
        return

    list_shapes(shapes)
    index = int(input("Enter the index of the shape to delete: ")) - 1
    if 0 <= index < len(shapes):
        del shapes[index]
        print("Shape deleted successfully.")
    else:
        print("Invalid index. Please select a valid shape.")

def menu():
    shapes = []
    while True:
        print("\n1. Create Shape\n2. List Shapes\n3. Modify Shape\n4. Delete Shape\n5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            shape = create_shape()
            if shape:
                shapes.append(shape)
        elif choice == "2":
            list_shapes(shapes)
        elif choice == "3":
            modify_shape(shapes)
        elif choice == "4":
            delete_shape(shapes)
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
