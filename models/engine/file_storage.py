#!/usr/bin/python3
"""<Filestorage> module: This module models the class for obj. storage"""
from json import loads, dumps
from os.path import exists


class FileStorage:
    """
    <Filestorage: This is the class for storage of object

    Attr:
        __objects: Stores the obj with key <obj class name>.id
        __file_path: string - path to the JSON file
    """
    __objects = {}
    __file_path = 'file.json'
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
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {}

        # Add the class name and convert datetime to isoformat str
        # Using 'to_dict' method in base_model class
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()

        # Serialize the obj_dict and write to .json file
        json_str = dumps(obj_dict)
        with open(FileStorage.__file_path, 'w') as f:
            f.write(json_str)

    def reload(self):
        """
            deserializes the JSON file to __objects (only if the JSON file
            (__file_path) exists ; otherwise, do nothing. If the file doesn’t
            exist, no exception should be raised)
        """
        # Import here to avoid circular import
        from models.base_model import BaseModel
        from models.user import User
        
        if exists(FileStorage.__file_path):
            json_str = ""
            with open(FileStorage.__file_path, "r") as file:
                json_str = file.read()
            obj_dict_store = loads(json_str)

            # Convert obj_dict back to object
            for key, obj_dict in obj_dict_store.items():
                if obj_dict["__class__"] == "BaseModel":
                    obj = BaseModel(**obj_dict)
                elif obj_dict["__class__"] == "Users":
                    obj = User(**obj_dict)
                    
                FileStorage.__objects[key] = obj
