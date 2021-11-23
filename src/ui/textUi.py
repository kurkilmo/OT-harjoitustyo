from data.metadata_subprocess import Metadata_subprocess

def run():
    cont = True
    dataTool = Metadata_subprocess()

    def read(inp):
        file = str(inp[1])
        mtd = dataTool.getMetadata(file)
        for item in mtd.keys():
            print(f"{item} --- {mtd[item]}")

    def write(inp):
        file = input("File to edit: ")
        tag = input("Metadata tag to edit: ")
        value = input("New value for metadata: ")
        success = dataTool.setMetadata(file, tag, value)
        if success:
            print("Editing succesful")
        else:
            print("Editing failed")


    print("Commands:\nread [file] - read metadata from file. Leave file field empty for example file\nwrite - edit a file's metadata\nexit - exit program")
    
    while(cont):
        inp = str(input("Command: "))
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
        elif inp[0] == "write":
            write(inp)
        else:
            print("Unknown command")

#run()