import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

#An update action that handles interactions between the actors.
#The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
#with the food, or the snake collides with its segments, or the game is over.

class HandleCollisionsAction(Action):
    
    def __init__(self):
        self._is_game_over = False
        
        # If true, red won, else green
        self._is_winner = False
#Executes the handle collisions action.
    def execute(self, cast, script):
        
        if not self._is_game_over:
            self.handle_food_collision(cast)
            self.handle_segment_collision(cast)
            self.handle_game_over(cast)
#Updates the score nd moves the food if the snake collides with the food.
    def handle_food_collision(self, cast):
        
        score = cast.get_first_actor("scores")
        food = cast.get_first_actor("foods")
        snake = cast.get_first_actor("snakes")
        red_snake = cast.get_first_actor("snake_red")
        red_head = red_snake.get_head()
        head = snake.get_head()

        if head.get_position().equals(food.get_position()):
            points = food.get_points()
            snake.grow_tail(points)
            score.add_points(points)
            food.reset()
        
        elif red_head.get_position().equals(food.get_position()):
            points = food.get_points()
            red_snake.grow_tail(points)
            score.add_points(points)
            food.reset()
#Sets the game over flag if the snake collides with one of its segments
    def handle_segment_collision(self, cast):
       
        snake = cast.get_first_actor("snakes")
        red_snake = cast.get_first_actor("snake_red")
        head = snake.get_segments()[0]
        segments = snake.get_segments()[1:]
        red_head = red_snake.get_head()
        red_segments = red_snake.get_segments()[1:]
        
        for segment in segments:
            if head.get_position().equals(segment.get_position()):
                self._is_game_over = True
                self._is_winner = True
            
            if head.get_position().equals(red_head.get_position()):
                self._is_game_over = True
        

            if red_head.get_position().equals(segment.get_position()):
                self._is_game_over = True
                

        for red_segment in red_segments :
            if red_head.get_position().equals(red_segment.get_position()):
                self._is_game_over = True
                self._is_winner = True
            
            if head.get_position().equals(red_segment.get_position()):
                self._is_game_over = True
                self._is_winner = True
#Shows the 'game over' message and turns the snake and food white if the game is over.
    def handle_game_over(self, cast):
        
        if self._is_game_over:
            snake = cast.get_first_actor("snakes")
            red_snake = cast.get_first_actor("snake_red")
            segments = snake.get_segments()
            food = cast.get_first_actor("foods")
            red_head = red_snake.get_head()
            red_segments = red_snake.get_segments()[1:]

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            if self._is_winner == True :
                message.set_text("Game Over! \nPlayer 2 Wins!")
            
            elif self._is_winner == False :
                message.set_text("Game Over! \nPlayer 1 Wins!")
            
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments:
                segment.set_color(constants.WHITE)
            
            for red_segment in red_segments:
                red_segment.set_color(constants.WHITE)
            
            food.set_color(constants.WHITE)