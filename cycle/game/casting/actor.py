import constants
from game.shared.color import Color
from game.shared.point import Point
"""A visible, moveable thing that participates in the game. 
    
    The responsibility of Actor is to keep track of its appearance, position and velocity in 2d 
    space.

    Attributes:
        _text (string): The text to display
        _font_size (int): The font size to use.
        _color (Color): The color of the text.
        _position (Point): The screen coordinates.
        _velocity (Point): The speed and direction.
    """

class Actor:
    
    #Constructs a new Actor.
    def __init__(self):
       
        self._text = ""
        self._font_size = 15
        self._color = Color(255, 255, 255)
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)
    #Gets the actor's color as a tuple of three ints (r, g, b).
    def get_color(self):
       
        return self._color
    #Gets the actor's font size.
    def get_font_size(self):
        
        return self._font_size
    #Gets the actor's position in 2d space.
    def get_position(self):
        
        return self._position
    #Gets the actor's textual representation.
    def get_text(self):
        
        return self._text
    #Gets the actor's speed and direction.
    def get_velocity(self):
        
        return self._velocity
    #Moves the actor to its next position according to its velocity. Will wrap the position 
    #from one side of the screen to the other when it reaches the given maximum x and y values.
    def move_next(self):
        
        x = (self._position.get_x() + self._velocity.get_x()) % constants.MAX_X
        y = (self._position.get_y() + self._velocity.get_y()) % constants.MAX_Y
        self._position = Point(x, y)

    #Updates the color to the given one.
    def set_color(self, color):
        
        self._color = color
    #Updates the position to the given one.
    def set_position(self, position):
        
        self._position = position
    #Updates the font size to the given one.
    def set_font_size(self, font_size):
        
        self._font_size = font_size
    #Updates the text to the given value.
    def set_text(self, text):
        
        self._text = text
    #Updates the velocity
    def set_velocity(self, velocity):
        
        self._velocity = velocity