import unittest
from ..data.metadata_subprocess import Metadata_subprocess

class TestMetadata(unittest.TestCase):
    def setUp(self):
        self.metadata = Metadata_subprocess()

    def test_getMetadata(self):
        file = "src/tests/eric.jpg"
        data = self.metadata.getMetadata(file)
        self.assertEqual(data["Image Width"], "300")