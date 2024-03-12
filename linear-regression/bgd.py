from typing import List

class BGD:
    def __init__(self, x: List[List[int]], y: List[int], w: List[int])->None:
        self.x = x
        self.y = y
        self.w = w

    def BGD(self, steps: int)->List[float]:
        for i in range(steps):
            pass