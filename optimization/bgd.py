from typing import List

class BGD:
    def __init__(self, x: List[List[int]], y: List[int], w: List[float], alpha: float)->None:
        self.x = x
        self.y = y
        self.w = w
        self.alpha = alpha

    def BGD(self)->None:
        n = len(self.y)

        for i in range(n):

            sum_vec = []
            temp_array = []

            for j in range(n):
                temp_array.append((self.w[i] * self.x[i][j]) - self.y[j])

            for j in range(n):
                sum_vec.append(temp_array[j] * self.x[i][j])

            all_sum = sum(sum_vec)
            self.w[i] = self.w[i] - ((2*self.alpha) * all_sum)

    def iteration(self, steps: int)->None:
        for i in range(steps):
            self.BGD()
            print(self.w)

x = [[1, 1, 1], [1, 2, 3], [1, 3, 5]]
y = [5, 13, 21]
w = [0, 0, 0]
a = 0.01
bgd = BGD(x, y, w, a)
bgd.iteration(2)