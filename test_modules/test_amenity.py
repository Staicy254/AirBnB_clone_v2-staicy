#!/usr/bin/python3
"""Tests for the Amenity model."""

import os
from tests.test_models.test_base_model import TestBasemodel
from models.amenity import Amenity


class TestAmenity(TestBasemodel):
    """Represents -- tests for the Amenity model."""

    def __init__(self, *args, **kwargs):
        """Initializes the test class."""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Tests -- type and value of name based on environment."""
        new = self.value()
        self.assertEqual(type(new.name), str)  # Always assert string type

        # Check for additional property or value based on environment variable
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            # Example: Test for a specific value or property set in 'db' mode
            self.assertIsNotNone(new.name)  # Assert name is not None in 'db' mode
        else:
            # Example: Test for a specific behavior in non-db mode
            self.assertLessEqual(len(new.name), 64)  # Assert name length <= 64

