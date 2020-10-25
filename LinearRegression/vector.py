class Vector(object):
    def __init__(self, size):
        """Creates a vector that stores a list of values, the average and its size"""
        self.data = [0 for x in range(size)]
        self.size = size
        self.average = 0

    def avg(self):
        """calculates the average of the vector"""
        for i in range(self.size):
            self.average += self.data[i]

        self.average /= self.size
        self.average = round(self.average, 3)

    def updateVals(self):
        """takes the input and updates the list within the vector"""
        for i in range(self.size):
            self.data[i] = int(input())
        self.avg()

    def changeVals(self, list):
        """updates the values for a given list"""
        for i in range(self.size):
            self.data[i] = list[i]

    def updateLen(self, len):
        """changes the length of the vector"""
        self.size = len
        self.data = [0 for x in range(len)]


    






