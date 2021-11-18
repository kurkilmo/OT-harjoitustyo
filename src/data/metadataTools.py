from hachoir.parser import createParser
from hachoir.metadata import extractMetadata

class Metadata:

    def __init__(self):
        a = 1

    def getMetadata(self, file):
        parser = createParser(file)
        
        mtd = dict()

        for line in extractMetadata(parser).exportPlaintext():
            split = str(line).split(":")
            split[0] = split[0][2:len(split[0])]
            split[1] = split[1][1:len(split[1])]
            mtd[split[0]] = split[1]

        return(mtd)

    