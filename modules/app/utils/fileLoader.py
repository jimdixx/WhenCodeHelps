class Loader:

    def __init__(self, fileName):
        self.fName = fileName
        self.loadedData = []

    def loadData(self):
        data = []
        shorts = {"např.": "například", "Např.": "například", "tzn.": "to znamená",
                  "Tzn.": "to znamená"}
        with open(self.fName) as f:
            lines = f.readlines()
            for line in lines:
                split = line.split(" ")
                for index, w in enumerate(split):
                    if w in list(shorts.keys()):
                        w = w.replace(w, shorts[w])
                        tmp = w.split()
                        if((isinstance(tmp, list)) and (len(tmp)>1)):
                            w = w.split()
                            split.pop(index)
                            split.insert(index, (w[0] + " " + w[1]))
                    if((isinstance(w, list)) and (len(w) > 1)):
                        data.append(w[0] + ". " + w[1] + ".")
                    else:
                        data.append(w + ".")

        # fonetic transcription
        sentence = ""
        banned = ["v.", "s.", "z.", "v:."]
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

