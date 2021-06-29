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
        """
        Check if its created properly
        """
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_is_str(self):
        """
        Check if id is of type string
        """
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_datatime(self):
        """
        Check if the datatime created_at is set up properly 
        """
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_different_id(self):
        """
        Checking for different id of different instance"""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_save(self):
        """
        Check if it save well
        """
        bm = BaseModel()
        sleep(0.05)
        time = bm.created_at
        bm.save()
        self.assertEqual(time, bm.created_at)

    def test_doc(self):
        """
        Check if documentation exists
        """
        self.assertNotEqual(len(BaseModel.__doc__), 0)
        self.assertNotEqual(len(BaseModel.__init__.__doc__), 0)
        self.assertNotEqual(len(BaseModel.__str__.__doc__), 0)
        self.assertNotEqual(len(BaseModel.save.__doc__), 0)
        self.assertNotEqual(len(BaseModel.to_dict.__doc__), 0)
        

    def test_str(self):
        """
        Testing str
        """
        b1 = BaseModel()
        self.assertEqual("[{}] ({}) {}".format(b1.__class__.__name__, b1.id, b1.__dict__), str(b1))

if __name__ == "__main__":
    unittest.main()
