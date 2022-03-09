import constants
from game.scripting.action import Action
from game.shared.point import Point
from game.services.keyboard_service import KeyboardService

#An input action that controls the snake.
class ControlActorsActionRed(Action):
    
#Constructs a new ControlActorsAction using the specified KeyboardService
    def __init__(self, keyboard_service: KeyboardService):
        
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)

#Executes the control actors action
    def execute(self, cast, script):
        
        # left
        if self._keyboard_service.is_key_down('j'):
            self._direction = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('l'):
            self._direction = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('i'):
            self._direction = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('k'):
            self._direction = Point(0, constants.CELL_SIZE)
        
        red_snake = cast.get_first_actor("snake_red")
        red_snake.turn_head(self._direction)