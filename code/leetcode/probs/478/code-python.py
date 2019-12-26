class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        
        # Safe solution with Reject Sampling
        # ans = float('inf')
        # while ans > self.r*self.r:
        #     x = self.x + random.random()*2*self.r - self.r
        #     y = self.y + random.random()*2*self.r - self.r
        #     ans = pow(x - self.x, 2) + pow(y - self.y, 2)
        # return [x, y]
        
        r = math.sqrt(random.random())*self.r # sqrt is used to have uniform distribution
        deg = random.random()*math.pi*2
        x = self.x + math.cos(deg)*r
        y = self.y + math.sin(deg)*r
        return [x, y]