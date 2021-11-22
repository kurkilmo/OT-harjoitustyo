import subprocess
from data.metadataTools import Metadata
from data.metadata_subprocess import Metadata_subprocess


def run():
    cont = True

    def read(inp):
        dataTool = Metadata_subprocess()
        file = str(inp[1])
        mtd = dataTool.getMetadata(file)
        for item in mtd.keys():
            print(f"{item} --- {mtd[item]}")


    print("Commands:\nread (file) - read metadata from file. Leave file field empty for example file\nexit - exit program")
    
    while(cont):
        inp = input("Command: ")
        if str(inp) == 'read':
            inp = 'read testimage.jpg'
        #inp = "read testailua/ormus.jpg"
        inp = str(inp).split(" ")

        if inp[0] == "read":
            try:
                read(inp)
            except:
                print("File not found or invalid file")
        elif inp[0] == "exit":
            cont = False
            return
        else:
            print("Unknown command")