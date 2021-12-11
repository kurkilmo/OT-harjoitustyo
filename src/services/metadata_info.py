import sqlite3

class MetadataInfo:
    """Class for finding information about metadata tags from a database.
    """
    def __init__(self):
        self.database = sqlite3.connect("src/data/exiftooldb.db")

    def check_writable(self, tag: str):
        """Check if given metadata tag is writable.

        Args:
            tag (str): Metadata tag to check

        Returns:
            True, if tag is readable and False if not.
        """
        result = self.database.execute(
            "SELECT writable FROM Datainfo WHERE attribute = ?",
            [tag]
        ).fetchall()

        if not result:
            result = "True"
        else:
            result = str(result[0])[2:-3]

        return result != "False"

    def check_type(self, tag: str):
        """Find the data type of given metadata tag.

        Args:
            tag (str): Metadata tag to check

        Returns:
            "string", if tag values are strings,
            "num", if tag values are numerical,
            None if tag is not writable.
        """
        result = self.database.execute(
            "SELECT writable FROM Datainfo WHERE attribute = ?",
            [tag]
        ).fetchall()

        if not result:
            result = "True"
        else:
            result = str(result[0])[2:-3]

        if result == "True":
            return "string"
        if result == "num":
            return "num"

        return None
