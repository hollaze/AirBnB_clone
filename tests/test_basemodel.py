#!/usr/bin/python3
""" Test module """
from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    """
    Test for class BaseModel
    """
    def test_if_exist(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_save(self):
        bm = BaseModel()
        update_time = bm.updated_at
        bm.save()
        self.assertLess(update_time, bm.updated_at)
        
    #def test_to_dict(self):

    #def test_id(self):

    #def test_created_at(self):

    #def test_str(self):

    #def test_init(self):

if __name__ == "__main__":
    unittest.main()
