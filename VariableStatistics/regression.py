from vector import Vector
class LinearRegression(object):
    def __init__(self, size):
        self.size = size
        self.SSxx = 0
        self.SSxy = 0
        self.SSyy = 0
        self.bhat0 = 0
        self.bhat1 =0
        self.SSE =0

    def update_bhat1(self):
        self.bhat1 = self.SSxy/self.SSxx

    def update_bhat0(self, xlist, ylist):
        self.bhat0 = ylist.average - xlist.average*self.bhat1

    def update_vals(self, xlist, ylist):
        self.update_bhat1()
        self.update_bhat0(xlist, ylist)
    
    def errorList(self, xlist, ylist):
        

        e = [0 for i in range(self.size)]
        for i in range(self.size):
            e[i] = ylist[i] - self.bhat1 * xlist[i] -self.bhat0
                
        errors = Vector(self.size)
        errors.changeVals(e)
        return errors
