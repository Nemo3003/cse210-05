"""A color.

    The responsibility of Color is to hold and provide information about itself. Color has a few 
    convenience methods for comparing them and converting to a tuple.

    Attributes:
        _red (int): The red value.
        _green (int): The green value.
        _blue (int): The blue value.
        _alpha (int): The alpha or opacity.
    """
class Color:
    
#Constructs a new Color using the specified red, green, blue and alpha values. The alpha 
#value is the color's opacity.
    def __init__(self, red, green, blue, alpha = 255):
        
        self._red = red
        self._green = green
        self._blue = blue 
        self._alpha = alpha
#Gets the color as a tuple of four values (red, green, blue, alpha).
    def to_tuple(self):
        
        return (self._red, self._green, self._blue, self._alpha)   