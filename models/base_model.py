#!/usr/bin/python3

"""
creating a class called BaseModel
"""
from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """
    Represent a class BaseModel
    """

    def __init__(self, *args, **kwargs):
        """
        Initializing the case BaseModel
        """
        datetime_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, datetime_format))
                else:
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

        models.storage.new(self)

    def save(self):
        """
        updates the attribute updated_at to the current datetime
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        serialization: converting instance into dictionary
        """
        current_dict = self.__dict__.copy()
        current_dict["__class__"] = self.__class__.__name__

        current_dict["created_at"] = self.created_at.isoformat()
        current_dict["updated_at"] = self.updated_at.isoformat()

        return current_dict

    def __str___(self):
        """
        returns a string representation  of the dictionary
        """
        current_class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(current_class_name, self.id, self.__dict__)


my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))


print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)
