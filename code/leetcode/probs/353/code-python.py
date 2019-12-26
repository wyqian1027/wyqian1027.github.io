class SnakeGame:

    
    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        init = [(0, 0)]
        self.snake = collections.deque(init)
        self.snakeSet = set(init)
        self.food = collections.deque(food)
        self.w = width
        self.h = height
        self.currentFood = tuple(self.food.popleft()) if self.food else None
        self.currentPos = (0, 0)
        self.score = 0
        self.d = {'U': (-1, 0), 'L': (0, -1), 'R': (0, 1), 'D': (1, 0)}

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        r, c = self.currentPos
        dr, dc = self.d[direction]
        nr, nc = r+dr, c+dc
        if nr < 0 or nr >= self.h or nc < 0 or nc >= self.w:
            return -1
        else:
            self.currentPos = nr, nc
            self.snake.append(self.currentPos)
            
            # remove tail first
            if self.currentPos == self.currentFood:
                self.score += 1
                self.currentFood = tuple(self.food.popleft()) if len(self.food) else None
            else:
                self.snakeSet.remove(self.snake.popleft())
            
            # then check head, because head could be at tail position, => cycle
            if self.currentPos in self.snakeSet: 
                return -1
            else:
                self.snakeSet.add(self.currentPos)
        return self.score