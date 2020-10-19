from vector import Vector
class LinearRegression(object):
    def __init__(self, size):
        #initalization of the class with most of the variables set to 0
        self.size = size
        self.SSxx = 0
        self.SSxy = 0
        self.SSyy = 0
        self.bhat0 = 0
        self.bhat1 =0
        self.SSE =0
        self.SSTO =0
        self.SSR =0
        self.var = 0
        self.sd =0
        self.rSquared = 0
        self.r =0

    def update_bhat1(self):
        #Calculates the value of bhat1
        self.bhat1 = self.SSxy/self.SSxx

    def update_bhat0(self, xlist, ylist):
        #Calculates the value of bhat0
        self.bhat0 = ylist.average - xlist.average*self.bhat1

    def update_vals(self, xlist, ylist):
        #Calls the two previous values to update the values
        self.update_bhat1()
        self.update_bhat0(xlist, ylist)
    
    def errorList(self, xlist, ylist):
        """Creates the error vector and returns it.
        In order to do so, we need to have the x vector and y vector.
        Calculates the expected y value for a given x and then subracts
        it from the actual y value to get the size of the error"""

        e = [0 for i in range(self.size)]
        for i in range(self.size):
            e[i] = ylist[i] - self.bhat1 * xlist[i] -self.bhat0
                
        errors = Vector(self.size)
        errors.changeVals(e)
        return errors
