#!/usr/bin/python3
"""Tests for the City model."""

from models.city import City
from tests.test_models.test_base_model import TestBasemodel
import os


class TestCity(TestBasemodel):
    """Represents = tests for City model."""

    def __init__(self, *args, **kwargs):
        """Initializes test class."""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Tests type of state_id."""
        new = self.value()
        self.assertEqual(
            type(new.state_id),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_name(self):
        """Tests type of name."""
        new = self.value()
        self.assertEqual(
            type(new.name),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

