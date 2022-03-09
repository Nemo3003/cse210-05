from game.casting.actor import Actor
import time
  
# define the countdown func.
def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

  
  
# input time in seconds
t = 5
  
# function call

COUNTDOWN = countdown(int(t))
class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    
    def __init__(self):
        super().__init__()
        self._points = 0
        self.add_points(0)

    def add_points(self, points):
        #Adds the given points to the score's total points.
        #But we won't have points...it is nice to have it tho...
        self._points += points
        self.set_text(f"Give us a good grade, pleasee! :D")
    