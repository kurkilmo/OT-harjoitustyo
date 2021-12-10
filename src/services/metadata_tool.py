import subprocess


class MetadataTool:
    """Class for reading and writing a file's metadata.
    """
    def __init__(self):
        self.exe = 'exiftool'

    def get_metadata(self, file):
        """Read metadata from a file.

        Args:
            file: Path to desired file

        Returns:
            A dictionary containing metadata attributes as keys and values as values.
        """
        process = subprocess.Popen([self.exe, file],
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)

        mtd = {}

        for data in process.stdout:
            data = str(data)
            split = data.split(': ')

            split[0] = split[0][2:len(split[0])].strip()
            split[1] = split[1][0:-3].strip()

            mtd[split[0]] = split[1]

        return mtd

    def set_metadata(self, file, tag, value):
        """Write metadata to a file.

        Args:
            file: Path to desired (existing) file.
            tag: Metadata attribute to change
            value: New value for attribute

        Returns:
            True, if writing was succesful and False if not.
        """
        tag = str(tag).replace(" ", "")
        args = f'-{tag}={value}'
        success = True
        output = subprocess.run([self.exe, args, file],
                              stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT)
        output = str(output.stdout.decode())
        if output.find("1 image files updated") == -1:
            success = False

        return success
