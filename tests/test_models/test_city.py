#!/usr/bin/python3

from models.city import City
from datetime import datetime
import unittest
from unittest import mock


class Test_City_Attributes(unittest.TestCase):
    
    def test_city_id(self):
        city = City()
        self.assertEqual(str, type(city.state_id))
        self.assertEqual(city.state_id, "")
        
    def test_user_id(self):
        city = City()
        self.assertEqual(str, type(city.name))
        self.assertEqual(city.name, "")
        
class Test_City_Instantiation(unittest.TestCase):
    def test_if_exist(self):
        """
        Check if its created properly
        """
        self.assertEqual(City, type(City()))

    def test_type(self):
        """
        Check if id is of type string
        Check if the datatime created_at is set up properly 
        """
        city = City()
        self.assertEqual(str, type(city.id))
        self.assertEqual(datetime, type(city.created_at))

    def test_differents(self):
        """
        Checking for different id, updated_at, created_at of different instance"""
        c1 = City()
        c2 = City()
        self.assertNotEqual(c1.id, c2.id)
        self.assertNotEqual(c1.updated_at, c2.updated_at)
        self.assertNotEqual(c1.created_at, c2.created_at)
        
    def test_str(self):
        """
        Testing str
        """
        p1 = City()
        self.assertEqual("[{}] ({}) {}".format(p1.__class__.__name__, p1.id, p1.__dict__), str(p1))

    @mock.patch('models.storage')
    def test_save(self, mock_storage):
        """Test that save method updates `updated_at` and calls
        `storage.save`"""
        inst = City()
        old_created_at = inst.created_at
        old_updated_at = inst.updated_at
        inst.save()
        new_created_at = inst.created_at
        new_updated_at = inst.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertEqual(old_created_at, new_created_at)
        self.assertTrue(mock_storage.save.called)
        
    def test_keys_to_dict(self):
        city = City()
        self.assertEqual(type(city.__dict__), dict)
        self.assertIn("__class__", city.to_dict())
        self.assertIn("created_at", city.to_dict())
        self.assertIn("updated_at", city.to_dict())
        self.assertIn("id", city.to_dict())
        
    def test_new_key_to_dict(self):
        city = City()
        city.name = "Holberton"
        city.my_number = 89
        self.assertIn("name", city.to_dict())
        self.assertIn("my_number", city.to_dict())
                
if __name__ == '__main__':
    unittest.main()
