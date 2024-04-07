import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    def test_new_instance_added_to_storage(self):
        storage = FileStorage()
        initial_count = len(storage.all())  # Get the initial count of objects in storage
        obj = BaseModel()
        # Check that the object is added to storage after instantiation
        self.assertEqual(len(storage.all()), initial_count + 1)
        self.assertIn("BaseModel." + obj.id, storage.all())  # Check if object is in storage


if __name__ == '__main__':
    unittest.main()
