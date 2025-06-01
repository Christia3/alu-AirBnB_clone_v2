import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_instance_creation(self):
        """Test if an instance is created properly."""
        try:
            instance = BaseModel()
            self.assertIsInstance(instance, BaseModel)
        except Exception as e:
            self.fail(f"Unexpected exception occurred: {e}")
