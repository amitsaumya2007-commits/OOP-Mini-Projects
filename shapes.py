from abc import ABC, abstractmethod
from math import pi
class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass
    def __lt__(self,other):
        if not isinstance(other,Shape):
             return NotImplemented
        return self.area() < other.area()
    
        
class Circle(Shape):
    def __init__(self, radius:float):
        self.radius = radius
    def area(self):
        return round(float(pi*self.radius**2),3)
    def __repr__(self):
        return f"Circle(radius={self.radius})"

class Square(Shape):
    def __init__(self,side:float):
        self.side = side
    def area(self):
        return float(self.side**2)
    def __repr__(self):
            return f"Square(side={self.side})"

class Rectangle(Shape):
    def __init__(self,length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return float(self.length*self.breadth)
    def __repr__(self):
            return f"Rectangle(length={self.length}, breadth={self.breadth})"

class Triangle(Shape):
    def __init__(self,side_1:float,side_2:float):
        self.side_1 = side_1
        self.side_2 = side_2
    def area(self):
        return float(0.5*self.side_1*self.side_2)
    def __repr__(self):
            return f"Triangle(side_1={self.side_1}, side_2={self.side_2})"

def total_area(shapes:list)-> float:
    total_area = sum(map(lambda s: s.area(), shapes))
    return total_area

rectangle = Rectangle(3,5)
circle = Circle(3)
square = Square(8)
triangle = Triangle(4,5)

# print(f"Rectangle's area: {rectangle.area()}")
# print(f"Circle's area: {circle.area()}")
# print(rectangle.area() < circle.area())

shapes_list = [rectangle,square,circle,triangle]

sorted_shapes = list(sorted(shapes_list))
print(sorted_shapes)

print(total_area(shapes_list))

# Inheritance is the process of inheriting methods and attributes form a parent class 
# to a subclass for the sake of code reusability and following DRY. Polymorphism on 
# the other hand is very closely related to inheritance(even uses inheritance), but 
# it's purpose is to make some interfaces like methods of abstract classes to provide 
# related classes with common and reusable features. In inheritance, classes are strongly 
# related( child class cannot work without parent class) but in polymorphism, classes
# are loosely related( all the classes are independent even after using polymorphism) 

