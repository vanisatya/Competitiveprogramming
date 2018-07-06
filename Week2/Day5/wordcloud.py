class WordCloudData(object):
    def __init__(self, inp):
        l = re.split('\.| |\?|\!|:|\- |, |\(|\)',inp)
        dct = {}
        for i in l:
            if i!='':
                j = i.title()
                if i in dct:
                    dct[i] += 1
                elif j in dct:
                    dct[i] = 1+dct[j]
                    dct.pop(j, None)
                else:
                    dct[i] = 1
        self.words_to_counts = dct