import constants
from game.casting.actor import Actor
from game.shared.point import Point
from game.casting.snake import Snake
"""
    This is the second player ::)
    
    Here we construct the snake. movements, head, tail, segments, everything's here
    """

class Snake_Red(Snake):
    
    def __init__(self):
        super().__init__()
        self._segments = []
        self.prepare_body()

    
    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(constants.RED)
            self._segments.append(segment)
    
    def prepare_body(self):
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text =  "#"
            color = constants.YELLOW if i == 0 else constants.RED
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)