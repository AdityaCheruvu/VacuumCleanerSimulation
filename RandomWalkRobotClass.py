class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        self.direction=random.uniform(0,360)
        newpos=self.pos.getNewPosition(self.direction, self.speed)
        if(self.room.isPositionInRoom(newpos)==False):
            self.direction=random.uniform(0,360)
        else:
            self.pos=newpos
        self.room.cleanTileAtPosition(self.pos)

