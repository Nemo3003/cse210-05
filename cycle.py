# import the pygame module
import pygame

# Define the background colour
# using RGB color coding.
class Window:
    def background(self):
        # Fill the background colour to the screen
        background_colour = (0, 0, 0)
        screen.fill(background_colour)
        # Define the dimensions of
        # screen.
        screen = pygame.display.set_mode((600, 600))

        # Set the caption of the screen
        pygame.display.set_caption('Cycle Game')
        pygame.display.flip()
        running = True
        # game loop
        while running:
            # for loop through the event queue
	        for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
class First_Player:

    def name(self):
        # Define the player's name
        player_name = input("Enter your name: ")
        return player_name
    def colour(self):
        # Define the player's colour
        player_colour = input("Enter your colour: ")
        return player_colour
    
class Second_Player:
    def name(self):
        player_name = input("Enter your name: ")
        return player_name
    def colour(self):
        player_colour = input("Enter your colour: ")
        return player_colour

first = First_Player()
second = Second_Player()
def asking(obj):
    print("Hello", obj.name())
    print("Your colour is", obj.colour())

asking(first)
asking(second)