import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

   

class Character(Base):
    __tablename__= 'character'
    name = Column(String(100), primary_key=True)
    alternate_names = Column(String(100))
    house = Column(String(50), nullable=False)
    date_of_birth = Column(String(100))
    patronus = Column(String(100))
    half_bood = Column(Boolean)
    actor = Column(String(100))
    favorite = relationship ("favorite")

class User(Base):
    __tablename__= 'user'
    username = Column (String (50), primary_key=True)
    name = Column (String(100), nullable=False)
    email = Column (String(100), nullable=False)
    favorite = relationship ("favorite")

class Favorite(Base):
    __tablename__= 'favorite'
    id = Column (String (50), primary_key=True)
    character_name = Column (String(100), ForeignKey('character.name'))
    character_username = Column (String(100), ForeignKey('user.username'))

   
##def to_dict(self):
        ##return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
