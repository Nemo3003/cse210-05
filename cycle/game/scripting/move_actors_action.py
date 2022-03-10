from game.scripting.action import Action


class MoveActorsAction(Action) :
    def __init__(self) -> None:
        super().__init__()
    
    def execute(self, cast, script):
        actors = cast.get_all_actors()
        for i in actors:
            i.move_next()