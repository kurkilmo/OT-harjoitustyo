from services.metadata_tool import MetadataTool # pylint: disable=import-error


def run():
    cont = True
    datatool = MetadataTool()

    def read(inp):
        file = str(inp[1])
        mtd = datatool.get_metadata(file)
        for item in mtd.keys():
            print(f"{item} --- {mtd[item]}")

    def write():
        file = input("File to edit: ")
        tag = input("Metadata tag to edit: ")
        value = input("New value for metadata: ")
        success = datatool.set_metadata(file, tag, value)
        if success:
            print("Editing succesful")
        else:
            print("Editing failed")

    print("Commands:")
    print(
        "read [file] - read metadata from file. Leave file field empty for example file")
    print("write - edit a file's metadata\nexit - exit program")

    while cont:
        inp = str(input("Command: "))
        if str(inp) == 'read':
            inp = 'read testimage.jpg'
        #inp = "read testailua/ormus.jpg"
        inp = str(inp).split(" ")

        if inp[0] == "read":
            read(inp)
        elif inp[0] == "exit":
            cont = False
            return
        elif inp[0] == "write":
            write()
        else:
            print("Unknown command")
