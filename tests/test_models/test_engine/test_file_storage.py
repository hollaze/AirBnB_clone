#!/usr/bin/python3

from models.engine.file_storage import FileStorage
import models
import unittest


class Test_FileStorage(unittest.TestCase):
    def test_if_exist(self):
        self.assertEqual(models.FileStorage, type(models.FileStorage()))

    def test__file_path(self):
        filestorage = models.FileStorage()
        self.assertEqual(str, type(filestorage._FileStorage__file_path))

    def test__objects(self):
        filestorage = models.FileStorage()
        self.assertEqual(dict, type(filestorage._FileStorage__objects))

    def test_all(self):
        filestorage = models.FileStorage()
        self.assertGreater(len(filestorage._FileStorage__objects), 0)


if __name__ == '__main__':
    unittest.main()
