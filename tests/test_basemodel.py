#!/usr/bin/python3
""" Test module """
import models
import os
import unittest
from time import sleep
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Test for class BaseModel
    """
    def test_if_exist(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_is_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_different_id(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_created_at_is_datatime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_save(self):
        bm = BaseModel()
        sleep(0.05)
        time = bm.created_at
        bm.save()
        self.assertEqual(time, bm.created_at)
        

    #def test_to_dict(self):

    #def test_id(self):

    #def test_created_at(self):

    #def test_str(self):

    #def test_init(self):

if __name__ == "__main__":
    unittest.main()
