#!/usr/bin/python3

from models.state import State
from datetime import datetime
import unittest
from unittest import mock


class Test_State_Attributes(unittest.TestCase):

    def test__name(self):
        state = State()
        self.assertEqual(str, type(state.name))
        self.assertEqual(state.name, "")
        
class Test_State_Instantiation(unittest.TestCase):
    def test_if_exist(self):
        """
        Check if its created properly
        """
        self.assertEqual(State, type(State()))

    def test_type(self):
        """
        Check if id is of type string
        Check if the datatime created_at is set up properly 
        """
        state = State()
        self.assertEqual(str, type(state.id))
        self.assertEqual(datetime, type(state.created_at))

    def test_differents(self):
        """
        Checking for different id, updated_at, created_at of different instance"""
        s1 = State()
        s2 = State()
        self.assertNotEqual(s1.id, s2.id)
        self.assertNotEqual(s1.updated_at, s2.updated_at)
        self.assertNotEqual(s1.created_at, s2.created_at)
        
    def test_str(self):
        """
        Testing str
        """
        s1 = State()
        self.assertEqual("[{}] ({}) {}".format(s1.__class__.__name__, s1.id, s1.__dict__), str(s1))

    @mock.patch('models.storage')
    def test_save(self, mock_storage):
        """Test that save method updates `updated_at` and calls
        `storage.save`"""
        inst = State()
        old_created_at = inst.created_at
        old_updated_at = inst.updated_at
        inst.save()
        new_created_at = inst.created_at
        new_updated_at = inst.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertEqual(old_created_at, new_created_at)
        self.assertTrue(mock_storage.save.called)
        
    def test_keys_to_dict(self):
        state = State()
        self.assertEqual(type(state.__dict__), dict)
        self.assertIn("__class__", state.to_dict())
        self.assertIn("created_at", state.to_dict())
        self.assertIn("updated_at", state.to_dict())
        self.assertIn("id", state.to_dict())
        
    def test_new_key_to_dict(self):
        state = State()
        state.name = "Holberton"
        state.my_number = 89
        self.assertIn("name", state.to_dict())
        self.assertIn("my_number", state.to_dict())
                
if __name__ == '__main__':
    unittest.main()
