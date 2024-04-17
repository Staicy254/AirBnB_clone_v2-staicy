#!/usr/bin/python3
"""Tests for the State model."""

from models.state import State
from tests.test_models.test_base_model import TestBasemodel
import os


class TestState(TestBasemodel):
    """Represents = tests for - State model."""

    def __init__(self, *args, **kwargs):
        """Initializes the test class."""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name(self):
        """Tests type of name."""
        new = self.value()
        self.assertEqual(
            type(new.name),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

