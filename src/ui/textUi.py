from data.metadataTools import Metadata


def run():
    cont = True

    def read(inp):
        dataTool = Metadata()
        file = str(inp[1])
        mtd = dataTool.getMetadata(file)
        for item in mtd.keys():
            print(f"{item} --- {mtd[item]}")



    
    while(cont):
        inp = input("Command: ")
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