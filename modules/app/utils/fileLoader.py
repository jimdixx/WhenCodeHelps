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
        # fonetic transcription
        sentence = ""
        banned = ["v.", "s.", "z.", "v:."]
        samohlasky = ["a", "e", "i", "o", "u"]
        for idx, w in enumerate(data):
            ls = list(w)
            if not (ls[-1] == "." and ls[-2] == "."):
                word = data[idx].lower()
                data[idx] = word
            sentence += w + " "

        for idx, w in enumerate(data):
            if w in banned:
                data[idx + 1] = data[idx].replace(".", "") + "" + data[idx + 1]
                data.pop(idx)
        return data

