import unittest
from models.engine.db_storage import DBStorage


class TestDBStorage(unittest.TestCase):
    """Test cases for the DBStorage class."""

    def test_storage_instance(self):
        """Test if storage is an instance of DBStorage."""
        storage = DBStorage()
        self.assertIsInstance(storage, DBStorage)

    def test_new_method(self):
        """Test the new method of DBStorage."""
        obj = SomeModel(name="Test")
        storage = DBStorage()
        storage.new(obj)
        self.assertIn(obj, storage.all().values())

    def test_save_method(self):
        """Test the save method of DBStorage."""
        obj = SomeModel(name="Test")
        storage = DBStorage()
        storage.new(obj)
        storage.save()
        self.assertIn(obj, storage.all().values())
