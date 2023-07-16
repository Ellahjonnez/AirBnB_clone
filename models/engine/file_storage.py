#!/usr/bin/python3
"""This function defines the FileStorage class."""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User


class FileStorage:
    """
    serializes the JSON File instances and
    deserializes JSON file to instances
    """

    _file_path = "file.json"
    _objects = {}

    def all(self):
        """Return the dictionary _objects."""
        return FileStorage._objects

    def new(self, obj):
        """Set in _objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage._objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serialize _objects to the JSON file."""
        odict = FileStorage._objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage._file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file _file_path to __objects, if it exists."""
        try:
            with open(FileStorage._file_path) as f:
                objdict = json.load(f)
                for obj in objdict.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            return
