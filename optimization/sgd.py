from typing import List

class SGD:
    def __init__(self, x: List[List[int]], y: List[int], w: List[float], alpha: float)->None:
        self.x = x
        self.y = y
        self.w = w
        self.alpha = alpha

    def sgd(self, j) -> None:
        n = len(self.w)
        for i in range(n):
            y = self.y[j]
            xji = self.x[j][i]
            self.w[i] = self.w[i] - ( ( 2 * self.alpha) * (( (self.w[i] * xji) - y) * xji) )

    def iteration(self, steps, j) -> None:
        for i in range(steps):
            self.sgd(j)
            print(self.w)

x = [ [1, 4], [2, 5], [3, 6] ]
y = [2, 4, 8]
w = [0, 0]
a = 0.01

sGD = SGD(x, y, w, a)
sGD.iteration(2, 1)


