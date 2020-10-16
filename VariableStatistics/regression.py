from vector import Vector
class LinearRegression(object):
    def __init__(self, size):
        self.size = size
        self.SSxx = 0
        self.SSxy = 0
        self.SSyy = 0
        self.bhat0 = 0
        self.bhat1 =0

    def update_vals(self, xlist, ylist):
        self.update_bhat1
        self.update_bhat2

    def update_bhat1(self):
        self.bhat1 = self.SSxy/self.SSxx

    def update_bhat2(self, xlist, ylist):
        self.bhat0 = ylist.average - xlist.average*bhat1

    def errorList(self, xlist, ylist):
        

        errors = Vector(self.size)
        for i in range(self.size):
            errors.data = ylist[i] -self.bhat1*xlist[i] -self.bhat0

        return errors
