#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime


class BaseModel:

    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
        if kwargs is not None:
            #dans la sortie, self.created_at & self.updated_at sont str
            #hors, on veut en datetime
            #si j'enlève cette condition, ça fonctionne comme il faut
            #j'ai essayé avec la ligne d'en dessous mais là je vais me coucher
            self.created_at = datetime.strptime(self.created_at, '%Y/%m/%d/%H/%M/%S/%f') #Ne fonctionne pas
            self.__dict__.update(kwargs) # Si j'ai bien compris, cette ligne est ok
        
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            

    def __str__(self):
        return "[{}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        key = self.__class__.__name__
        for key in self.__dict__.keys():
            return self.__dict__

