class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        if(self.room.isPositionInRoom(self.pos.getNewPosition(self.direction, self.speed))==False):
            self.direction=random.uniform(0,360)
        else:
            x=self.pos.getNewPosition(self.direction,self.speed)
            self.pos=Position(x.getX(), x.getY())
        self.room.cleanTileAtPosition(self.pos)

