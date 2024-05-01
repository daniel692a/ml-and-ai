from typing import List

class BGD:
    def __init__(self, x: List[List[int]], y: List[int], w: List[float], alpha: float)->None:
        self.x = x
        self.y = y
        self.w = w
        self.alpha = alpha

    def BGD(self)->None:
        n = len(self.w)
        m = len(self.y)

        for i in range(n):

            sum_vec = []
            temp_array = []

            for j in range(m):
                temp_array.append((self.w[i] * self.x[i][j]) - self.y[j])

            for j in range(m):
                sum_vec.append(temp_array[j] * self.x[i][j])

            all_sum = sum(sum_vec)
            self.w[i] = self.w[i] - ((2*self.alpha) * all_sum)

    def iteration(self, steps: int)->None:
        for i in range(steps):
            self.BGD()
            print(self.w)

x = [[468.0, 616.0, 594.0, 625.0, 963.0, 440.0, 255.0]]
y = [1.08, 1.42, 1.37, 1.44, 2.21, 1.01, 0.59]
w = [0]
a = 0.01
bgd = BGD(x, y, w, a)
bgd.iteration(4)