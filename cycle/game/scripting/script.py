"""A collection of actions.

    The responsibility of Script is to keep track of a collection of actions. It has methods for 
    adding, removing and getting them by a group name.

    """
class Script:
    
    def __init__(self):
 
        self._actions = {}
#Adds an action to the group
    def add_action(self, group, action):
        
        if not group in self._actions.keys():
            self._actions[group] = []
            
        if not action in self._actions[group]:
            self._actions[group].append(action)
#Gets the actions in the  group.
    def get_actions(self, group):
        results = []
        if group in self._actions.keys():
            results = self._actions[group].copy()
        return results
    #Removes an action from the group
    def remove_action(self, group, action):
        
        if group in self._actions:
            self._actions[group].remove(action)