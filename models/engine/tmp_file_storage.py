#!/usr/bin/python3
"""This module defines the FileStorage class"""
import json


class FileStorage:
    """FileStorage class that serializes/deserializes instances to/from JSON"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of all stored objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file"""
        my_dict = {}
        for key, value in FileStorage.__objects.items():
            my_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """Deserialize the JSON file to __objects if it exists"""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                my_dict = json.load(f)
            for key, value in my_dict.items():
                pass
        except FileNotFoundError:
            pass
