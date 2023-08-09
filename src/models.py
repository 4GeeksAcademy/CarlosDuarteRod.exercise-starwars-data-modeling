import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable = True)
    url = Column(String(600), nullable = True)

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable = True)
    url = Column(String(600), nullable = True)

    class Followers(Base):
         __tablename__ = 'followers'
    User_from_id = Column(Integer, ForeignKey('user.id'))
    User_to_id = Column(Integer, ForeignKey("user.id") , nullable = True)

    class User(Base):
         __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable = True)
    firstname = Column(String(250), nullable = True)
    lasttname = Column(String(250), nullable = False)
    email = Column(String(300), nullable = True)

    class Favorites(Base):
         __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable = True)
    url = Column(String(250), nullable = True)
    user_id = Column(Integer,ForeignKey('user.id'), nullable = True)

    class Comment(Base):
         __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(600), nullable = True)
    author_id = Column(Integer,ForeignKey('user.id'), nullable = True)
    post_id = Column(Integer, ForeignKey('post.user_id'), nullable = True)

    class Post(Base):
         __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable = True)
    user_id = Column(Integer,ForeignKey('user.id'), nullable = True)

    class Media(Base):
         __tablename__ = 'media'
    id = Column(Integer, primary_key = True)
    type = Column(enumerate, nullable = True)
    url = Column(String, nullable = True)
    post_id = Column(Integer,ForeignKey('post.id'), nullable = True)
   
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
