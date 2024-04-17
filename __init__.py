#!/usr/bin/python3
"""Tests for AirBnb clone modules."""

import os
from typing import TextIO
from models.engine.file_storage import FileStorage


def clear_stream(stream: TextIO) -> None:
    """Clears contents of a given stream.

    Args:
        stream (TextIO): The stream to clear.
    """
    if stream.seekable():
        stream.seek(0)
        stream.truncate(0)


def delete_file(file_path: str) -> None:
    """Removes file if it exists.

    Args:
        file_path (str): The name of the file to remove.
    """
    if os.path.isfile(file_path):
        os.remove(file_path)


def reset_store(store: FileStorage, file_path: str = 'file.json') -> None:
    """Resets the items in the given store.

    Args:
        store (FileStorage): The FileStorage to reset.
        file_path (str, optional): The path to the store's file.
            Defaults to 'file.json'.
    """
    with open(file_path, mode='w') as file:
        file.write('{}')
    if store is not None:
        store.reload()


def read_text_file(file_name: str) -> str:
    """Reads the contents of a given file.

    Args:
        file_name (str): Name - file to read.

    Returns:
        str: The contents of the file if it exists.
    """
    if os.path.isfile(file_name):
        with open(file_name, mode='r') as file:
            return file.read()
    return ''


def write_text_file(file_name: str, text: str) -> None:
    """Writes a text to a given file.

    Args:
        file_name (str): Name - file to write to.
        text (str): The content of the file.
    """
    with open(file_name, mode='w') as file:
        file.write(text)


# Unique code - Function to check if objects exist in storage
def object_exists_in_storage(cls, obj_id: str) -> bool:
    """
    Checks if an object with the given ID exists in storage.

    Args:
        cls: The class of the object to check.
        obj_id:  ID - object to check.

    Returns:
        bool: True if 0bject exists, False otherwise.
    """
    all_objs = storage.all(cls)
    return any(obj.id == obj_id for obj in all_objs.values())


# Example usage of the unique function
# Replace SomeClass with the appropriate class name from your project
result = object_exists_in_storage(SomeClass, "some_id")
print(f"The result of the unique function is: {result}")

