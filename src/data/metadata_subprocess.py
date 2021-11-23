import subprocess
import os

class Metadata_subprocess:
    def __init__(self):
        self.exe = 'exiftool'

    def getMetadata(self, file):
        process = subprocess.Popen([self.exe, file], stdout=subprocess.PIPE, stderr = subprocess.STDOUT)

        mtd = {}

        for data in process.stdout:
            data = str(data)
            split = data.split(': ')

            split[0] = split[0][2:len(split[0])].strip()
            split[1] = split[1][0:-3].strip()

            mtd[split[0]] = split[1]

        return(mtd)

    def setMetadata(self, file, tag, value):
        args = f'-{tag}={value}'
        output = subprocess.run([self.exe, args, file], stdout=subprocess.PIPE, stderr = subprocess.STDOUT)
        output = str(output.stdout.decode())

        success = True
        if output.find("1 image files updated") == -1:
            success = False
        
        return success