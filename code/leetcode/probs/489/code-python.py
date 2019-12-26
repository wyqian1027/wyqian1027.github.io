# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        DIRECTIONS = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        visited = set()
        def go_back():
            robot.turnLeft()
            robot.turnLeft()
            robot.move()
            robot.turnLeft()
            robot.turnLeft()
            
        def backtrack(pos, cur_dir):
            robot.clean()
            visited.add(tuple(pos))
            for _ in range(4):
                new_pos = [pos[0] + DIRECTIONS[cur_dir][0],
                           pos[1] + DIRECTIONS[cur_dir][1]]
                if tuple(new_pos) not in visited and robot.move():
                    backtrack(new_pos, cur_dir)
                    go_back()
                robot.turnRight()
                cur_dir = (cur_dir + 1 ) % 4
        
        backtrack([0, 0], 0)