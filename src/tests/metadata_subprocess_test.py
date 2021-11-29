import unittest
from ..services.metadata_tool import MetadataTool


class TestMetadata(unittest.TestCase):
    def setUp(self):
        self.metadata = MetadataTool()

    def test_get_metadata(self):
        file = "src/tests/eric.jpg"
        data = self.metadata.get_metadata(file)
        self.assertEqual(data["Image Width"], "300")
