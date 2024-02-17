#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        # Initialize a FileStorage instance
        self.storage = FileStorage()

    def test_new_and_all(self):
        # Test if adding a new BaseModel instance results in it being in the storage
        obj = BaseModel()
        self.storage.new(obj)
        self.assertIn("BaseModel." + obj.id, self.storage.all())

    def test_save_and_reload(self):
        # Test if saving and reloading retains the same objects
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()
        self.assertIn("BaseModel." + obj.id, new_storage.all())

    def tearDown(self):
        # Clean up any temporary files or resources
        pass


if __name__ == '__main__':
    unittest.main()
