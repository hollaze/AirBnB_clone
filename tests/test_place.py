#!/usr/bin/python3

import models
from models.base_model import BaseModel
from models.place import Place
from datetime import datetime
import unittest


class Test_Place(unittest.TestCase):
    place = Place()
    
    def test_types_attributes(self):
        self.assertEqual(str, type(Place().city_id))
        self.assertEqual(str, type(Place().user_id))
        self.assertEqual(str, type(Place().description))
        self.assertEqual(str, type(Place().name))
        self.assertEqual(int, type(Place().number_rooms))
        self.assertEqual(int, type(Place().number_bathrooms))
        self.assertEqual(int, type(Place().max_guest))
        self.assertEqual(int, type(Place().price_by_night))
        self.assertEqual(float, type(Place().latitude))
        self.assertEqual(float, type(Place().longitude))
        self.assertEqual(list, type(Place().amenity_ids))
                
if __name__ == '__main__':
    unittest.main()