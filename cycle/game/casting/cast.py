from game.casting.actor import Actor
"""A collection of actors.

    The responsibility of a cast is to keep track of a collection of actors. It has methods for 
    adding, removing and getting them by a group name.

    Attributes:
        _actors (dict): A dictionary of actors { key: group_name, value: a list of actors }
    """

class Cast:
    #A collection of actors.
    def __init__(self):
        
        self._actors = {}
    #Adds an actor to the given group.
    def add_actor(self, group, actor):
        
        if not group in self._actors.keys():
            self._actors[group] = []
            
        if not actor in self._actors[group]:
            self._actors[group].append(actor)
    #Gets the actors in the same group.
    def get_actors(self, group):
        
        results = []
        if group in self._actors.keys():
            results = self._actors[group].copy()
        return results
    #Gets all of the actors in the cast.
    def get_all_actors(self):
        
        results = []
        for group in self._actors:
            results.extend(self._actors[group])
        return results
    #gets the first actor
    def get_first_actor(self, group):
        result = None
        if group in self._actors.keys():
            result = self._actors[group][0]
        return result
    #Removes an actor from the group
    def remove_actor(self, group, actor):
        
        if group in self._actors:
            self._actors[group].remove(actor)