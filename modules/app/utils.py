def preprocess_words(text):
    words = [word for sentence in text.split(".") for word in sentence.split()]
    souhlasky = ["v", "s", "z", "k"]
    i = 0
    while i < len(words) - 1:
        if words[i] in souhlasky:
            words[i] = words[i] + words[i + 1]
            del words[i + 1]
        else:
            i += 1
    return words