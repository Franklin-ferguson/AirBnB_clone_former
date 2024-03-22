#!/usr/bin/python3
"""
Creating a file storage
"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """
    Represents a class FileStorage
    """

    __file_path = "file.json"
    __objects = {}


    def new(self, obj):
        """
        adds new attributes to the dictionary
        """
    
        object_class_name = obj.__class__.__name__

        key = "{}.{}".format(object_class_name, obj.id)

        FileStorage.__object[key] = obj

    def all(self):
        """
        returns all ojects
        """
        return FileStorage.__objects

    def dave(self):
        """
        serialize the dictionary into json stirng
        """
        full_object_list = FileStorage.__objects

        full_dict = {}

        for obj in full_object_list:
            full_dict[obj] = full_object_list[obj].to_dict()

        with open(FileStorage.__file_path, 'w', encoding="utf-8") as files:
            json.dump(full_dict, files)

        def reload(self):
            """
            Deserializing the json string back to dictionary
            """
            if os.path.isfile(FileStorage.__file_path):
                with open(FileStorage.__file_path, 'r', encoding="utf-8") as files:
                    try:
                        full_dict = json.load(files)

                        for key, value in full_dict.items():
                            inst_class, obj_id = key.split('.')

                            class_name = eval(inst_class)

                            object_instance = class_name(**values)

                            File.Storage.__object[key] = object_instance
                    except Exception:
                        pass























