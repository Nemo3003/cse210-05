import random
import constants
from game.casting.actor import Actor
from game.shared.point import Point
"""
    An item that will help our snakes to grow
    
    The responsibility of Food is to select a random position and points that it's worth.

    
    """

class Food(Actor):
    #FOOOOD
    def __init__(self):
        super().__init__()
        self._points = 0
        self.set_text("")
        self.set_color(constants.RED)
        self.reset()
    #Selects a random position and points that the food is worth.
    def reset(self):
        
        self._points = random.randint(1, 8)
        x = random.randint(1, constants.COLUMNS - 1)
        y = random.randint(1, constants.ROWS - 1)
        position = Point(x, y)
        position = position.scale(constants.CELL_SIZE)
        self.set_position(position)
    #How much does your food is worth it?
    def get_points(self):
        
        return self._points