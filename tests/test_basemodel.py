#!/usr/bin/python3
""" Test module """
import models
import os
import unittest
from unittest import mock
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

    def test_type(self):
        """
        Check if id is of type string
        Check if the datatime created_at is set up properly 
        """
        self.assertEqual(str, type(BaseModel().id))
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_differents(self):
        """
        Checking for different id, updated_at, created_at of different instance"""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)
        self.assertNotEqual(b1.updated_at, b2.updated_at)
        self.assertNotEqual(b1.created_at, b2.created_at)

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

    @mock.patch('models.storage')
    def test_save(self, mock_storage):
        """Test that save method updates `updated_at` and calls
        `storage.save`"""
        inst = BaseModel()
        old_created_at = inst.created_at
        old_updated_at = inst.updated_at
        inst.save()
        new_created_at = inst.created_at
        new_updated_at = inst.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertEqual(old_created_at, new_created_at)
        self.assertTrue(mock_storage.save.called)

if __name__ == "__main__":
    unittest.main()
