import unittest
from ..services.metadata_info import MetadataInfo

class TestMetadataInfo(unittest.TestCase):
    def setUp(self):
        self.info = MetadataInfo()

    def test_writable_returns_true(self):
        self.assertTrue(self.info.check_writable("Artist"))

    def test_writable_returns_false(self):
        self.assertFalse(self.info.check_writable("File Name"))

    def test_type_returns_none(self):
        self.assertIsNone(self.info.check_type("Directory"))

    def test_type_returns_num(self):
        self.assertEqual(self.info.check_type("Compression"), "num")

    def test_type_returns_string(self):
        self.assertEqual(self.info.check_type("Make"), "string")

    def test_writable_returns_true_on_unknown_attribute(self):
        self.assertTrue(self.info.check_writable("oidhgofdahgj"))

    def test_type_returns_string_on_unknown_attribute(self):
        self.assertEqual(self.info.check_type("oisjfdoisahoijg"), "string")
