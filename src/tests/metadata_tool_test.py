import unittest
from ..services.metadata_tool import MetadataTool


class TestMetadata(unittest.TestCase):
    def setUp(self):
        self.metadata = MetadataTool()
        self.file = "src/tests/eric.jpg"

    def test_get_metadata(self):
        data = self.metadata.get_metadata(self.file)
        self.assertEqual(data["Image Width"], "300")

    def test_set_metadata_returns_true(self):
        succ = self.metadata.set_metadata(self.file, "author", "returntrue")
        self.assertTrue(succ)
        self._reset_author

    def test_set_metadata_returns_false_on_invalid_tag(self):
        succ = self.metadata.set_metadata(self.file, "invalidTag", "---")
        self.assertFalse(succ)

    def test_set_metadata_returns_false_on_unwritable_tag(self):
        succ = self.metadata.set_metadata(self.file, "filetype", "filetype")
        self.assertFalse(succ)

    def test_set_metadata_works(self):
        self.metadata.set_metadata(self.file, "author", "test")
        self.assertEqual(self.metadata.get_metadata(self.file)["Author"], "test")
        self._reset_author


    def _reset_author(self):
        self.metadata.set_metadata(self.file, "author", "exampleauthor")
