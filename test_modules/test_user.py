#!/usr/bin/python3
"""Tests for the User model."""

from models.user import User
from tests.test_models.test_base_model import TestBasemodel
import os


class TestUser(TestBasemodel):
    """Represents = tests for - User model."""

    def __init__(self, *args, **kwargs):
        """Initializes the test class."""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_email(self):
        """Tests - type of email."""
        new = self.value()
        self.assertEqual(
            type(new.email),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_first_name(self):
        """Tests - type of first_name."""
        new = self.value()
        self.assertEqual(
            type(new.first_name),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_last_name(self):
        """Tests - type of last_name."""
        new = self.value()
        self.assertEqual(
            type(new.last_name),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_password(self):
        """Tests - type of password."""
        new = self.value()
        self.assertEqual(
            type(new.password),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )
