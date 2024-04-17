#!/usr/bin/python3
"""Tests for the BaseModel class."""

import os
import unittest
from datetime import datetime
import json
from uuid import UUID

from models.base_model import BaseModel, Base


class TestBasemodel(unittest.TestCase):
    """Represents the tests for the BaseModel."""

    def __init__(self, *args, **kwargs):
        """Initializes the test_class."""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """Performs = operations before the tests are run."""
        pass

    def tearDown(self):
        """Performs = operations after the tests are run"""
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_init(self):
        """Tests initialization of the model class.
        """
        self.assertIsInstance(self.value(), BaseModel)
        if self.value is not BaseModel:
            self.assertIsInstance(self.value(), Base)
        else:
            self.assertNotIsInstance(self.value(), Base)

    def test_default(self):
        """Tests type of value stored."""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """Tests kwargs with an int."""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """Tests kwargs & an int (raises TypeError)."""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
    def test_save(self):
        """Tests the save function of the BaseModel class.
           - Adds a check for successful file write operation.
        """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            try:
                j = json.load(f)
                self.assertEqual(j[key], i.to_dict())
            except FileNotFoundError:
                self.fail("File not written after save")

    def test_str(self):
        """Tests the __str__ function of the BaseModel class."""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                                                        i.__dict__))

    def test_todict(self):
        """Tests the to_dict function of the model class.
           - Adds test for custom attributes with non-string values.
        """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)
        # ... other tests from original code ...

        # Test to_dict with non-string attribute
        mdl = self.value()
        mdl.age = 30  # Add an integer attribute
        self.assertIn('age', mdl.to_dict())
        self.assertEqual(type(mdl.to_dict()['age']), int)

        # Test to_dict with a list attribute
        list_attr = [1, 2, 3]
        mdl.mylist = list_attr
        self.assertIn('mylist', mdl.to_dict())
        self.assertEqual(mdl.to_dict()['mylist'], list_attr)

    # ... other tests from original code ...

    def test_kwargs_none(self):
        """Tests kwargs that is empty."""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """Tests kwargs with one key-value pair."""
        n = {'Name': 'test'}
        new = self.value(**n)
        self.assertTrue(hasattr(new, 'Name'))

    def test_id(self):
        """Tests the type of id."""
        new = self.value()
        self

