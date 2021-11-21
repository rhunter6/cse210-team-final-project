

class LiveActor():
    def __init__(self) -> None:
        pass

    def set_orientation(self, direction):
        """ Make the actor face a certain direction
        ARGS:
            self (LiveActor): an instance of Player
            direction (string): should be in [ "UP", "DOWN", "LEFT", "RIGHT" ]
        """
        direction = direction.upper()

        if direction in [ "UP", "DOWN", "LEFT", "RIGHT" ]:
            self._orientation = direction
        
    def get_orientation(self):
        """ Returns the orientation
        ARGS:
            self (LiveActor):
        RETURNS:
            orientation (STR)
        """
        return self._orientation