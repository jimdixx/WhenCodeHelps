class Loader:

    def __init__(self, fileName):
        self.fName = fileName
        self.loadedData = []

    def loadData(self):
        data = []
        with open(self.fName) as f:
            lines = f.readlines()
            for line in lines:
                split = line.split(" ")
                for w in split:
                    data.append(w + ".")
        return data