#!/usr/bin/python3

import models
from models.base_model import BaseModel
from models.place import Place
from datetime import datetime
import unittest


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
        
    
                
if __name__ == '__main__':
    unittest.main()