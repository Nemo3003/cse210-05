import random
from store import constants
from game.casting.actor import Actor
from game.shared.point import Point

#TODO: Maybe this should be deleted
class Food(Actor):
    #FOOOOD
    def __init__(self):
        "Constructs a new Food."
        super().__init__()
        self._points = 0
        self.set_text("Group 4 - CSE210")
        self.set_color(constants.RED)
        self.reset()
        
    def reset(self):
        #Selects a random position and points that the food is worth.
        self._points = random.randint(1, 8)
        x = random.randint(1, constants.COLUMNS - 1)
        y = random.randint(1, constants.ROWS - 1)
        position = Point(x, y)
        position = position.scale(constants.CELL_SIZE)
        self.set_position(position)
        
    def get_points(self):
        #Gets the points the food is worth.
        
        return self._points