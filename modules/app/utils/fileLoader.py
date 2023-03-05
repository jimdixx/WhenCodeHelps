import re
class Loader:

    def __init__(self, fileName = None):
        self.fName = fileName
        self.loadedData = []

    def loadData(self):
        data = []
        shorts = {"např.": "například", "Např.": "například", "tzn.": "to znamená",
                  "Tzn.": "to znamená", "t.j.": "to jest", "T.j.": "To jest",
                  "aj": "a jiné", "atd.": "a tak dále", "tzv.": "takzvaný", "str.": "strana",
                  "č": "číslo"}
        with open(self.fName) as f:
            lines = f.readlines()
            for idx, line in enumerate(lines):
                # deleting the unwanted characters
                edited_line = re.sub("\\\\n", "", line)
                pattern = re.compile("[^a-zA-Z0-9.+ěščřžýáíéĚŠČŘŽÝÁÍÉüůú]")
                edited_line = re.sub(pattern, " ", edited_line)
                edited_line = re.sub(r"\s{2,}", " ", edited_line.strip())
                split = edited_line.split(" ")
                if(idx == 0):
                    split = split[1:len(split)-2]
                for index, w in enumerate(split):
                    if w in list(shorts.keys()):
                        w = w.replace(w, shorts[w])
                        tmp = w.split()
                        if((isinstance(tmp, list)) and (len(tmp)>1)):
                            w = w.split()
                            split.pop(index)
                            split.insert(index, (w[0] + " " + w[1]))
                    if((isinstance(w, list)) and (len(w) > 1) and (len(w) <= 2)):
                        data.append(w[0] + ". " + w[1] + ".")
                    elif((isinstance(w, list)) and (len(w) > 2)):
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