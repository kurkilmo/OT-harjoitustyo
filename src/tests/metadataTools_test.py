import unittest
from ..data.metadataTools import Metadata

class TestMetadata(unittest.TestCase):
    def setUp(self):
        self.metadata = Metadata()

    def test_getMetadata(self):
        file = "src/tests/eric.jpg"
        data = self.metadata.getMetadata(file)
        self.assertEqual(data["Image width"], "300 pixels")