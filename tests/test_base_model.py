#!/usr/bin/python3
from models.base_model import BaseModel
import unittest

"""This file contains a class of test casing"""


class Testbase_models(unittest.TestCase):
    """Testing on BaseModels class"""

    def test__init__(self):
        obj = BaseModel()
        obj.name = "emma"
        return self.assertEqual(type(obj.name), str)

    def test_type(self):
        return self.assertNotEqual(type(BaseModel), type(BaseModel()))

    def test__str__(self):
        ob = BaseModel()
        ob.name = "emma"
        ob.my_number = 25
        return self.assertIn(ob.id, ob.__str__())

    def test_save(self):
        a = BaseModel()
        a.name = "emma"
        a.my_number = 23
        b = a.updated_at
        a.save()
        return self.assertNotEqual(b, a.updated_at)

    def test_dict(self):
        a = BaseModel()
        a.name = "emma"
        a.my_number = 23
        c = a.to_dict()
        return self.assertNotEqual(c, None)
