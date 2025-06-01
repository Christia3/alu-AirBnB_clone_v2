#!/usr/bin/python3
"""This module defines the FileStorage class."""
import json
import os


class FileStorage:
    """Serializes instances to a JSON file and deserializes back to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Returns a dictionary of all objects, or all objects of a specific class.

        Args:
            cls (type, optional): The class to filter by. Defaults to None.

        Returns:
            dict: Dictionary of objects.
        """
        if cls:
            return {
                key: obj
                for key, obj in self.__objects.items()
                if isinstance(obj, cls)
            }
        return self.__objects

    def new(self, obj):
        """Adds a new object to the storage dictionary."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        from models import storage
        with open(self.__file_path, "w") as f:
            json.dump(
                {
                    k: v.to_dict()
                    for k, v in self.__objects.items()
                }, f
            )

    def reload(self):
        """Deserializes the JSON file to __objects (only if the file exists)."""
        from models import classes
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                objs = json.load(f)
                for key, val in objs.items():
                    cls_name = val["__class__"]
                    self.__objects[key] = classes[cls_name](**val)

    def delete(self, obj=None):
        """
        Deletes obj from __objects if it's inside.

        Args:
            obj (object, optional): The object to delete. Defaults to None.
        """
        if obj is None:
            return
        key = f"{obj.__class__.__name__}.{obj.id}"
        if key in self.__objects:
            del self.__objects[key]
