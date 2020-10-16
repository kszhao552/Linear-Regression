class Vector(object):
    def __init__(self, size):
        self.data = [0 for x in range(size)]
        self.size = size
        self.average = 0

    def avg(self):
        for i in range(self.size):
            self.average += self.data[i]

        self.average /= self.size

    def updateVals(self):
        for i in range(self.size):
            self.data[i] = int(input())
        self.avg()

    def updateVals(self, list):
        for i in range(self.size):
            self.data[i] = list[i]
        self.avg



    






