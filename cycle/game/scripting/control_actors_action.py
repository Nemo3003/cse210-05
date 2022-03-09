import constants
from game.scripting.action import Action
from game.shared.point import Point
from game.services.keyboard_service import KeyboardService

#An input action that controls the snake.
#The responsibility of ControlActorsAction is to get the direction and move the snake's head.
class ControlActorsAction(Action):
    
#Constructs a new ControlActorsAction using the specified KeyboardService
    def __init__(self, keyboard_service: KeyboardService):
        
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)
#Executes the control actors action.
    def execute(self, cast, script):
        
        # left
        if self._keyboard_service.is_key_down('a'):
            self._direction = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('d'):
            self._direction = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('w'):
            self._direction = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('s'):
            self._direction = Point(0, constants.CELL_SIZE)
        
        snake = cast.get_first_actor("snakes")
        snake.turn_head(self._direction)