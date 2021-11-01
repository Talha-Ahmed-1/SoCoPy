def loadmemoryfromfile(pathToFile):
    file = open(pathToFile, "r")
    return tuple([int("0x"+inst, 16) for inst in open(pathToFile, "r").read().split("\n")])