#!/usr/bin/python3

import os
import unittest
import models
from models.user import User
from models.base_model import BaseModel

class TestUser(unittest.TestCase):

    def setUp(self):
        """temp test file for saving data"""
        self.test_file = "test_file.json"
        models.storage.__file_path = self.test_file
        models.storage.save()

    def tearDown(self):
        """remove temp test file"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_user_attributes(self):
        """test user attr and create new user instance"""
        test_user = User()
        self.assertEqual(test_user.email, "")
        self.assertEqual(test_user.password, "")
        self.assertEqual(test_user.first_name, "")
        self.assertEqual(test_user.last_name, "")

    def test_user_inheritance_from_base_model(self):
        """test user inheritance"""
        test_user = User()
        self.assertTrue(issubclass(User, BaseModel))

    def test_user_str_representation(self):
        """test, set attribs of user instance"""
        test_user = User()
        test_user.email = "airbnb@mail.com"
        test_user.first_name = "Betty"
        test_user.last_name = "Bar"
        test_user.password = "root"
        """get string rep and checks if User is present"""
        user_str = str(test_user)
        self.assertIn("User", user_str)
        self.assertIn("airbnb@mail.com", user_str)
        self.assertIn("Betty", user_str)
        self.assertIn("Bar", user_str)

    def test_user_to_dict(self):
        """dictionary rep of user instance"""
        test_user = User()
        test_user.email = "airbnb@mail.com"
        test_user.first_name = "Betty"
        test_user.last_name = "Bar"
        test_user.save()

        user_dict = test_user.to_dict()
        self.assertEqual(user_dict['email'], "airbnb@mail.com")
        self.assertEqual(user_dict['first_name'], "Betty")
        self.assertEqual(user_dict['last_name'], "Bar")

    def test_user_instance_creation(self):
        """creates new user instance with args"""
        test_user = User(email="airbnb@mail.com", password="root", first_name="Betty", last_name="Bar")
        """checks is user attr are set correct"""
        self.assertEqual(test_user.email, "airbnb@mail.com")
        self.assertEqual(test_user.password, "root")
        self.assertEqual(test_user.first_name, "Betty")
        self.assertEqual(test_user.last_name, "Bar")

    def test_user_instance_to_dict(self):
        """user instance to dict"""
        test_user = User(email="airbnb@mail.com", password="root", first_name="Betty", last_name="Bar")

        user_dict = test_user.to_dict()
        self.assertEqual(user_dict['email'], "airbnb@mail.com")
        self.assertEqual(user_dict['password'], "root")
        self.assertEqual(user_dict['first_name'], "Betty")
        self.assertEqual(user_dict['last_name'], "Bar")

    def test_user_id_genaration(self):
        """make sure id sttr os each user is unique"""
        test_user = User()
        user2 = User()
        self.assertNotEqual(test_user.id, user2.id)

if __name__ == '__main__':
    unittest.main()
