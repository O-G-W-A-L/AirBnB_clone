#!/usr/bin/python3
"""Unittest for review.py"""
import unittest
from models.review import Review
import datetime

class TestReview(unittest.TestCase):
    """Tests instances and methods from Review class"""

    def setUp(self):
        """Set up a Review instance for testing"""
        self.review = Review()

    def test_class_exists(self):
        """Test if Review class exists"""
        self.assertEqual(str(type(self.review)), "<class 'models.review.Review'>")

    def test_inheritance(self):
        """Test if Review is a subclass of BaseModel"""
        self.assertIsInstance(self.review, Review)

    def test_has_attributes(self):
        """Test if Review instance has required attributes"""
        attributes = ['place_id', 'user_id', 'text', 'id', 'created_at', 'updated_at']
        for attr in attributes:
            self.assertTrue(hasattr(self.review, attr))

    def test_attribute_types(self):
        """Test if attributes have correct types"""
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)
        self.assertIsInstance(self.review.id, str)
        self.assertIsInstance(self.review.created_at, datetime.datetime)
        self.assertIsInstance(self.review.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
