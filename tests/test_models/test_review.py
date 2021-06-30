#!/usr/bin/python3

from models import review
from models.review import Review
from datetime import datetime
import unittest
from unittest import mock


class Test_Review_Attributes(unittest.TestCase):

    def test_place_id(self):
        review = Review()
        self.assertEqual(str, type(review.place_id))
        self.assertEqual(review.place_id, "")

    def test_user_id(self):
        review = Review()
        self.assertEqual(str, type(review.user_id))
        self.assertEqual(review.user_id, "")

    def test_text(self):
        review = Review()
        self.assertEqual(str, type(review.text))
        self.assertEqual(review.text, "")


class Test_Review_Instantiation(unittest.TestCase):
    def test_if_exist(self):
        """
        Check if its created properly
        """
        self.assertEqual(Review, type(Review()))

    def test_type(self):
        """
        Check if id is of type string
        Check if the datatime created_at is set up properly
        """
        review = Review()
        self.assertEqual(str, type(review.id))
        self.assertEqual(datetime, type(review.created_at))

    def test_differents(self):
        """
        Checking for different id, updated_at, created_at
        of different instance
        """
        r1 = Review()
        r2 = Review()
        self.assertNotEqual(r1.id, r2.id)
        self.assertNotEqual(r1.updated_at, r2.updated_at)
        self.assertNotEqual(r1.created_at, r2.created_at)

    def test_str(self):
        """
        Testing str
        """
        r1 = Review()
        self.assertEqual("[{}] ({}) {}".format(
            r1.__class__.__name__, r1.id, r1.__dict__), str(r1))

    @mock.patch('models.storage')
    def test_save(self, mock_storage):
        """Test that save method updates `updated_at` and calls
        `storage.save`"""
        inst = Review()
        old_created_at = inst.created_at
        old_updated_at = inst.updated_at
        inst.save()
        new_created_at = inst.created_at
        new_updated_at = inst.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertEqual(old_created_at, new_created_at)
        self.assertTrue(mock_storage.save.called)

    def test_keys_to_dict(self):
        review = Review()
        self.assertEqual(type(review.__dict__), dict)
        self.assertIn("__class__", review.to_dict())
        self.assertIn("created_at", review.to_dict())
        self.assertIn("updated_at", review.to_dict())
        self.assertIn("id", review.to_dict())

    def test_new_key_to_dict(self):
        review = Review()
        review.name = "Holberton"
        review.my_number = 89
        self.assertIn("name", review.to_dict())
        self.assertIn("my_number", review.to_dict())


if __name__ == '__main__':
    unittest.main()
