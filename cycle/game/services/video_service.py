import pyray
import constants

"""Outputs the game state. The responsibility of the class of objects is to draw the game state 
    on the screen. 
    """
class VideoService:
    
#Constructs a new VideoService using the specified debug mode
    def __init__(self, debug = False):
       
        self._debug = debug
#Closes the window and releases all computing resources
    def close_window(self):

        pyray.close_window()
#Clears the buffer in preparation for the next rendering. This method should be called at
#the beginning of the game's output phase.
    def clear_buffer(self):
        
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
        if self._debug == True:
            self._draw_grid()
#Draws the given actor's text on the screen.
    def draw_actor(self, actor, centered=False):
        
        text = actor.get_text()
        x = actor.get_position().get_x()
        y = actor.get_position().get_y()
        font_size = actor.get_font_size()
        color = actor.get_color().to_tuple()

        if centered:
            width = pyray.measure_text(text, font_size)
            offset = int(width / 2)
            x -= offset
            
        pyray.draw_text(text, x, y, font_size, color)
#Draws the text for the given list of actors on the screen.
    def draw_actors(self, actors, centered=False):
        
        for actor in actors:
            self.draw_actor(actor, centered)
#Copies the buffer contents to the screen. This method should be called at the end of
#the game's output phase.
    def flush_buffer(self):
        pyray.end_drawing()
#Whether or not the window was closed by the user.
    def is_window_open(self):
        
        return not pyray.window_should_close()
#Opens a new window with the provided title.

    def open_window(self):
        
        pyray.init_window(constants.MAX_X, constants.MAX_Y, constants.CAPTION)
        pyray.set_target_fps(constants.FRAME_RATE)
#Draws a grid on the screen.
    def _draw_grid(self):

        for y in range(0, constants.MAX_Y, constants.CELL_SIZE):
            pyray.draw_line(0, y, constants.MAX_X, y, pyray.GRAY)
            
        for x in range(0, constants.MAX_X, constants.CELL_SIZE):
            pyray.draw_line(x, 0, x, constants.MAX_Y, pyray.GRAY)
    
    def _get_x_offset(self, text, font_size):
        width = pyray.measure_text(text, font_size)
        return int(width / 2)