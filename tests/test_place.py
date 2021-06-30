#!/usr/bin/python3

import models
from models.base_model import BaseModel
from models.place import Place
from datetime import datetime
import unittest
from unittest import mock


class Test_Place_Attributes(unittest.TestCase):
    
    def test_city_id(self):
        place = Place()
        self.assertEqual(str, type(place.city_id))
        self.assertEqual(place.city_id, "")
        
    def test_user_id(self):
        place = Place()
        self.assertEqual(str, type(place.user_id))
        self.assertEqual(place.user_id, "")
        
    def test_description(self):
        place = Place()
        self.assertEqual(str, type(place.description))
        self.assertEqual(place.description, "")
        
    def test_name(self):
        place = Place()
        self.assertEqual(str, type(place.name))
        self.assertEqual(place.name, "")
        
    def test_number_rooms(self):
        place = Place()
        self.assertEqual(int, type(place.number_rooms))
        self.assertEqual(place.number_rooms, 0)
        
    def test_number_bathrooms(self):
        place = Place()
        self.assertEqual(int, type(place.number_bathrooms))
        self.assertEqual(place.number_bathrooms, 0)
        
    def test_max_guest(self):
        place = Place()
        self.assertEqual(int, type(place.max_guest))
        self.assertEqual(place.max_guest, 0)
    
    def test_price_by_night(self):
        place = Place()
        self.assertEqual(int, type(place.price_by_night))
        self.assertEqual(place.price_by_night, 0)
        
    def test_latitude(self):
        place = Place()
        self.assertEqual(float, type(place.latitude))
        self.assertEqual(place.latitude, 0.0)
        
    def test_longitude(self):
        place = Place()
        self.assertEqual(type(place.longitude), float)
        self.assertEqual(place.longitude, 0.0)
        
    def test_amenity_ids(self):
        place = Place()
        self.assertEqual(type(place.amenity_ids), list)
        self.assertEqual(len(place.amenity_ids), 0)
        
class Test_Place_Instantiation(unittest.TestCase):
    def test_if_exist(self):
        """
        Check if its created properly
        """
        self.assertEqual(Place, type(Place()))

    def test_type(self):
        """
        Check if id is of type string
        Check if the datatime created_at is set up properly 
        """
        place = Place()
        self.assertEqual(str, type(place.id))
        self.assertEqual(datetime, type(place.created_at))

    def test_differents(self):
        """
        Checking for different id, updated_at, created_at of different instance"""
        p1 = Place()
        p2 = Place()
        self.assertNotEqual(p1.id, p2.id)
        self.assertNotEqual(p1.updated_at, p2.updated_at)
        self.assertNotEqual(p1.created_at, p2.created_at)
        
    def test_str(self):
        """
        Testing str
        """
        p1 = Place()
        self.assertEqual("[{}] ({}) {}".format(p1.__class__.__name__, p1.id, p1.__dict__), str(p1))

    @mock.patch('models.storage')
    def test_save(self, mock_storage):
        """Test that save method updates `updated_at` and calls
        `storage.save`"""
        inst = Place()
        old_created_at = inst.created_at
        old_updated_at = inst.updated_at
        inst.save()
        new_created_at = inst.created_at
        new_updated_at = inst.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertEqual(old_created_at, new_created_at)
        self.assertTrue(mock_storage.save.called)
                
if __name__ == '__main__':
    unittest.main()
