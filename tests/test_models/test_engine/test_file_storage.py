import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def test_storage_instance(self):
        """Test if storage is an instance of FileStorage."""
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)

    def test_new_method(self):
        """Test the new method of FileStorage."""
        obj = SomeModel(name="Test")
        storage = FileStorage()
        storage.new(obj)
        self.assertIn(obj, storage.all().values())

    def test_save_method(self):
        """Test the save method of FileStorage."""
        obj = SomeModel(name="Test")
        storage = FileStorage()
        storage.new(obj)
        storage.save()
        self.assertIn(obj, storage.all().values())
