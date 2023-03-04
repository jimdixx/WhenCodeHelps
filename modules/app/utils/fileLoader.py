import re
class Loader:

    def __init__(self, fileName=None):
        self.fName = fileName
        self.loadedData = []

    def setFile(self, fileName):
        self.fName = fileName

    def loadData(self):
        data = []
        shorts = {"např.": "například", "Např.": "například", "tzn.": "to znamená",
                  "Tzn.": "to znamená", "t.j.": "to jest", "T.j.": "To jest",
                  "aj": "a jiné", "atd.": "a tak dále", "tzv.": "takzvaný", "str.": "strana",
                  "č": "číslo"}
        with open(self.fName) as f:
            lines = f.readlines()
            for line in lines:
                # deleting the unwanted chars in the input file
                pattern = re.compile("[^a-zA-Z0-9.+ěščřžýáíéĚŠČŘŽÝÁÍÉü]")
                cleaned_string = pattern.sub(' ', line)
                cleaned_string = re.sub(' +', ' ', cleaned_string)
                cleaned_string = cleaned_string.lstrip()
                cleaned_string = cleaned_string.rstrip()
                split = cleaned_string.split(" ")
                for index, w in enumerate(split):
                    """
                    if(re.match('\d', w) and index >= 1):
                        char_before = split[index-1]
                        if(char_before.lower() == "po"):
                            w = "páté"
                    """
                    if w in list(shorts.keys()):
                        w = w.replace(w, shorts[w])
                        tmp = w.split()
                        if((isinstance(tmp, list)) and (len(tmp)>1)):
                            w = w.split()
                            split.pop(index)
                            split.insert(index, (w[0] + " " + w[1]))
                    if((isinstance(w, list)) and (len(w) > 1) and (len(w) <= 2)):
                        data.append(w[0] + ". " + w[1] + ".")
                    if((isinstance(w, list)) and (len(w) > 2)):
                        data.append(w[0] + ". " + w[1] + "." + w[2] + ".")
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

