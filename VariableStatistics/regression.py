from vector import Vector
class LinearRegression(object):
    def __init__(self, size):
        self.size = size
        self.SSxx = 0
        self.SSxy = 0
        self.SSyy = 0
        self.bhat0 = 0
        self.bhat1 =0

    def update_vals(self, xbar, ybar):
        self.bhat1 = SSxy/SSxx
        self.bhat0 = ybar - xbar*bhat1

        errors = Vector(self.size)
