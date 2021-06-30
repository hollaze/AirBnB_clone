#!/usr/bin/python3

from models.amenity import Amenity
from datetime import datetime
import unittest
from unittest import mock


class Test_Amenity_Attributes(unittest.TestCase):

    def test_name(self):
        amenity = Amenity()
        self.assertEqual(str, type(amenity.name))
        self.assertEqual(amenity.name, "")


class Test_Amenity_Instantiation(unittest.TestCase):
    def test_if_exist(self):
        """
        Check if its created properly
        """
        self.assertEqual(Amenity, type(Amenity()))

    def test_type(self):
        """
        Check if id is of type string
        Check if the datatime created_at is set up properly
        """
        amenity = Amenity()
        self.assertEqual(str, type(amenity.id))
        self.assertEqual(datetime, type(amenity.created_at))

    def test_differents(self):
        """
        Checking for different id, updated_at, created_at of different instance
        """
        a1 = Amenity()
        a2 = Amenity()
        self.assertNotEqual(a1.id, a2.id)
        self.assertNotEqual(a1.updated_at, a2.updated_at)
        self.assertNotEqual(a1.created_at, a2.created_at)

    def test_str(self):
        """
        Testing str
        """
        a1 = Amenity()
        self.assertEqual("[{}] ({}) {}".format(
            a1.__class__.__name__, a1.id, a1.__dict__), str(a1))

    @mock.patch('models.storage')
    def test_save(self, mock_storage):
        """Test that save method updates `updated_at` and calls
        `storage.save`"""
        inst = Amenity()
        old_created_at = inst.created_at
        old_updated_at = inst.updated_at
        inst.save()
        new_created_at = inst.created_at
        new_updated_at = inst.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertEqual(old_created_at, new_created_at)
        self.assertTrue(mock_storage.save.called)

    def test_keys_to_dict(self):
        amenity = Amenity()
        self.assertEqual(type(amenity.__dict__), dict)
        self.assertIn("__class__", amenity.to_dict())
        self.assertIn("created_at", amenity.to_dict())
        self.assertIn("updated_at", amenity.to_dict())
        self.assertIn("id", amenity.to_dict())

    def test_new_key_to_dict(self):
        amenity = Amenity()
        amenity.name = "Holberton"
        amenity.my_number = 89
        self.assertIn("name", amenity.to_dict())
        self.assertIn("my_number", amenity.to_dict())


if __name__ == '__main__':
    unittest.main()
