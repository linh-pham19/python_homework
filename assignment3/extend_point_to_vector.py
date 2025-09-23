import math

class Point:
    """Represents a point in 2D space with x and y coordinates."""
    
    def __init__(self, x, y):
        """Initialize a point with x and y coordinates."""
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        """Check equality between two points."""
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        """String representation of a point."""
        return f"Point({self.x}, {self.y})"
    
    def distance(self, other):
        """Calculate Euclidean distance to another point."""
        if not isinstance(other, Point):
            raise TypeError("Distance can only be calculated to another Point")
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    

class Vector(Point):
    """Represents a vector in 2D space, inheriting from Point."""
    
    def __str__(self):
        """Override string representation for vectors."""
        return f"Vector<{self.x}, {self.y}>"
    
    def __add__(self, other):
        """Override + operator for vector addition."""
        if not isinstance(other, Vector):
            raise TypeError("Vector addition requires another Vector")
        return Vector(self.x + other.x, self.y + other.y)
    
p1 = Point(3, 4)
p2 = Point(0, 0)
p3 = Point(3, 4)  # Same as p1

print(f"Point 1: {p1}")
print(f"Point 2: {p2}")
print(f"Point 3: {p3}")

print(f"Are Point 1 and Point 2 equal? {p1 == p2}")
print(f"Are Point 1 and Point 3 equal? {p1 == p3}")

print(f"\nDistance from {p1} to {p2}: {p1.distance(p2):.2f}")
print(f"Distance from {p2} to {p1}: {p2.distance(p1):.2f}")
print(f"Distance from {p1} to {p3}: {p1.distance(p3):.2f}")

# Create some vectors
v1 = Vector(2, 3)
v2 = Vector(1, -1)
v3 = Vector(0, 5)

print(f"Vector 1: {v1}")
print(f"Vector 2: {v2}")
print(f"Vector 3: {v3}")

print(f"\nVector Addition:")
v4 = v1 + v2
print(f"{v1} + {v2} = {v4}")
    
v5 = v2 + v3
print(f"{v2} + {v3} = {v5}")

v6 = v1 + v3
print(f"{v1} + {v3} = {v6}")

# Test that vectors still inherit Point methods
print(f"\n== Vector inherits Point methods ==")
print(f"v1 == v2: {v1 == v2}")
print(f"Distance from {v1} to {v2}: {v1.distance(v2):.2f}")
    
# Test equality between Vector and Point with same coordinates
p4 = Point(2, 3)
print(f"\nVector {v1} == Point {p4}: {v1 == p4}")
print(f"Distance from Vector {v1} to Point {p4}: {v1.distance(p4):.2f}")

print(f"\n== Chaining Vector Addition ==")
result = v1 + v2 + v3
print(f"{v1} + {v2} + {v3} = {result}")
