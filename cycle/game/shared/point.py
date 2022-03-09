"""A distance from a relative origin (0, 0).

    The responsibility of Point is to hold and provide information about itself. Point has a few 
    convenience methods for adding, scaling, and comparing them.

    Attributes:
        _x (integer): The horizontal distance from the origin.
        _y (integer): The vertical distance from the origin.
    """
class Point:
    
#Constructs a new Point using the specified x and y values.
    def __init__(self, x, y):
        
        self._x = x
        self._y = y
#Gets a new point that is the sum of this and the given one.
    def add(self, other):
        
        x = self._x + other.get_x()
        y = self._y + other.get_y()
        return Point(x, y)

    def equals(self, other):
        #Whether or not this Point is equal to the given one.

        return self._x == other.get_x() and self._y == other.get_y()

    def get_x(self):
        #Gets the horizontal distance.

        return self._x

    def get_y(self):
        #Gets the vertical distance.

        return self._y

    def reverse(self):
        #Reverses the point by inverting both x and y values.

        new_x = self._x * -1
        new_y = self._y * -1
        return Point(new_x, new_y)
#Scales the point by the provided factor.
    def scale(self, factor):

        return Point(self._x * factor, self._y * factor)