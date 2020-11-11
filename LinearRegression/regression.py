from vector import Vector
class Regression(object):
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
        self.f = 0

    def update_bhat1(self):
        #Calculates the value of bhat1
        self.bhat1 = round(self.SSxy/self.SSxx, 3)

    def update_bhat0(self, xlist, ylist):
        #Calculates the value of bhat0
        self.bhat0 = round(ylist.average - xlist.average*self.bhat1, 3)

    def update_vals(self, xlist, ylist):
        #Calls the two previous values to update the values
        self.update_bhat1()
        self.update_bhat0(xlist, ylist)
    
    def predictVal(self, val):
        return (self.bhat1 * val + self.bhat0)

    def errorList(self, ylist, predictedlist):
        """Creates the error vector and returns it.
        In order to do so, we need to have the x vector and y vector.
        Calculates the expected y value for a given x and then subracts
        it from the actual y value to get the size of the error"""

        e = [0 for i in range(self.size)]
        for i in range(self.size):
            e[i] = round(ylist[i] - predictedlist[i], 3)
                
        errors = Vector(self.size)
        errors.changeVals(e)
        return errors

    def yhatList(self, xlist):
        #Creates the list of the predicted values and returns it using the created regression and the x vector.
        yhat = Vector(self.size)
        for i in range(self.size):
            yhat.data[i] = round(self.predictVal(xlist[i]), 3)

        return yhat

    def fStat(self):
        #Calculates the f statistic and returns it
        #uses SSR as the MSR and variance as the MSE.
        try:
            self.f = round(self.SSR/self.var, 3)
        except ZeroDivisionError:
            self.f = float('inf')

    def updateLen(self, size):
        self.size = size