<<<<<<< HEAD
#!/usr/bin/python3

from models.user import User
from datetime import datetime
import unittest
from unittest import mock


class Test_user_Attributes(unittest.TestCase):

    def test_email(self):
        user = User()
        self.assertEqual(str, type(user.email))
        self.assertEqual(user.email, "")

    def test_password(self):
        user = User()
        self.assertEqual(str, type(user.password))
        self.assertEqual(user.password, "")

    def test_first_name(self):
        user = User()
        self.assertEqual(str, type(user.first_name))
        self.assertEqual(user.first_name, "")

    def test_last_name(self):
        user = User()
        self.assertEqual(str, type(user.last_name))
        self.assertEqual(user.last_name, "")


class Test_user_Instantiation(unittest.TestCase):
    def test_if_exist(self):
        """
        Check if its created properly
        """
        self.assertEqual(User, type(User()))

    def test_type(self):
        """
        Check if id is of type string
        Check if the datatime created_at is set up properly 
        """
        user = User()
        self.assertEqual(str, type(user.id))
        self.assertEqual(datetime, type(user.created_at))

    def test_differents(self):
        """
        Checking for different id, updated_at, created_at of different instance"""
        u1 = User()
        u2 = User()
        self.assertNotEqual(u1.id, u2.id)
        self.assertNotEqual(u1.updated_at, u2.updated_at)
        self.assertNotEqual(u1.created_at, u2.created_at)

    def test_str(self):
        """
        Testing str
        """
        u1 = User()
        self.assertEqual("[{}] ({}) {}".format(
            u1.__class__.__name__, u1.id, u1.__dict__), str(u1))

    @mock.patch('models.storage')
    def test_save(self, mock_storage):
        """Test that save method updates `updated_at` and calls
        `storage.save`"""
        inst = User()
        old_created_at = inst.created_at
        old_updated_at = inst.updated_at
        inst.save()
        new_created_at = inst.created_at
        new_updated_at = inst.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertEqual(old_created_at, new_created_at)
        self.assertTrue(mock_storage.save.called)

    def test_keys_to_dict(self):
        user = User()
        self.assertEqual(type(user.__dict__), dict)
        self.assertIn("__class__", user.to_dict())
        self.assertIn("created_at", user.to_dict())
        self.assertIn("updated_at", user.to_dict())
        self.assertIn("id", user.to_dict())

    def test_new_key_to_dict(self):
        user = User()
        user.name = "Holberton"
        user.my_number = 89
        self.assertIn("name", user.to_dict())
        self.assertIn("my_number", user.to_dict())


if __name__ == '__main__':
    unittest.main()
=======
#!/usr/bin/python3

from models.user import User
from datetime import datetime
import unittest
from unittest import mock


class Test_user_Attributes(unittest.TestCase):

    def test_email(self):
        user = User()
        self.assertEqual(str, type(user.email))
        self.assertEqual(user.email, "")

    def test_password(self):
        user = User()
        self.assertEqual(str, type(user.password))
        self.assertEqual(user.password, "")

    def test_first_name(self):
        user = User()
        self.assertEqual(str, type(user.first_name))
        self.assertEqual(user.first_name, "")

    def test_last_name(self):
        user = User()
        self.assertEqual(str, type(user.last_name))
        self.assertEqual(user.last_name, "")


class Test_user_Instantiation(unittest.TestCase):
    def test_if_exist(self):
        """
        Check if its created properly
        """
        self.assertEqual(User, type(User()))

    def test_type(self):
        """
        Check if id is of type string
        Check if the datatime created_at is set up properly
        """
        user = User()
        self.assertEqual(str, type(user.id))
        self.assertEqual(datetime, type(user.created_at))

    def test_differents(self):
        """
        Checking for different id, updated_at, created_at
        of different instance
        """
        u1 = User()
        u2 = User()
        self.assertNotEqual(u1.id, u2.id)
        self.assertNotEqual(u1.updated_at, u2.updated_at)
        self.assertNotEqual(u1.created_at, u2.created_at)

    def test_str(self):
        """
        Testing str
        """
        u1 = User()
        self.assertEqual("[{}] ({}) {}".format(
            u1.__class__.__name__, u1.id, u1.__dict__), str(u1))

    @mock.patch('models.storage')
    def test_save(self, mock_storage):
        """Test that save method updates `updated_at` and calls
        `storage.save`"""
        inst = User()
        old_created_at = inst.created_at
        old_updated_at = inst.updated_at
        inst.save()
        new_created_at = inst.created_at
        new_updated_at = inst.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertEqual(old_created_at, new_created_at)
        self.assertTrue(mock_storage.save.called)

    def test_keys_to_dict(self):
        user = User()
        self.assertEqual(type(user.__dict__), dict)
        self.assertIn("__class__", user.to_dict())
        self.assertIn("created_at", user.to_dict())
        self.assertIn("updated_at", user.to_dict())
        self.assertIn("id", user.to_dict())

    def test_new_key_to_dict(self):
        user = User()
        user.name = "Holberton"
        user.my_number = 89
        self.assertIn("name", user.to_dict())
        self.assertIn("my_number", user.to_dict())


if __name__ == '__main__':
    unittest.main()
>>>>>>> 9ba81a81e01c21bf41e2c4fe8b97bc96d968119c
