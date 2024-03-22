#!/usr/bin/python3
"""<Filestorage> module: This module models the class for obj. storage"""
from json import loads, dumps
import os


class FileStorage:
    """
    <Filestorage: This is the class for storage of object

    Attr:
        __objects: Stores the obj with key <obj class name>.id
        __file_path: string - path to the JSON file
    """
    __objects = {}
    __file_path = 'store_json.json'
    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """
        Stores the obj with key <obj class name>.id into __objects dicts

        Args:
            obj: The created object from a given class
        """
        class_name = obj.__class__.__name__
        key = f'{class_name}.{obj.id}'
        Filestorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {}
        
        # Add the class name and convert datetime to isoformat str
        #Using 'to_dict)' method in base_model class
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()

        # Serialize the obj_dict and write to .json file
        json_str = dumps(obj_dict)
        with open(FileStorage.__file_path, 'w') as f:
            f.write(json_str)
