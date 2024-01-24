from uuid import uuid4
from datetime import datetime
"""BaseModel class that defines all common attributes/methods for other clasess"""
class BaseModel:
  
    """Represents the BaseModel for Airbnb project"""
    def __init__(self,*args, **kwargs):
        """Initialize a new BaseModel"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for name, value in kwargs.items():
                if name =="created_at" or name == "updated_at":
                    self.__dict__[name] =datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[name] = value
    def __str__(self):
        """Returns a string representation of the BaseModel instance"""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
  
    def save(self):
        """Updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
    
    def to_dict(self):
        """Returns a dictionary containing all key/values of __dict__"""
        return{
            "id":self.id,
            "created_at":self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
            "updated_at":self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
            "__class__": self.__class__.__name__
        }
