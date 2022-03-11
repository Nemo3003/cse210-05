from game.scripting.action import Action

#An output action that draws all the actors.
class DrawActorsAction(Action):
#Constructs a new DrawActorsAction using the specified VideoService.
    def __init__(self, video_service):
        
        self._video_service = video_service
#Executes the draw actors action
    def execute(self, cast, script):
        
        score = cast.get_first_actor("scores")
        food = cast.get_first_actor("foods")
        snake = cast.get_first_actor("snakes")
        snake2 = cast.get_first_actor("snake_red")
        segments = snake.get_segments()
        segments2 = snake2.get_segments()
        messages = cast.get_actors("messages")

        self._video_service.clear_buffer()
        self._video_service.draw_actor(food)
        self._video_service.draw_actors(segments)
        self._video_service.draw_actors(segments2)
        self._video_service.draw_actor(score)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()