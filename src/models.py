import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False, unique=True)
    username = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    subscription_date = Column(String(250))

class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250))

class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(500))

class Favorito(Base):
    __tablename__ = 'favorito'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('usuario.id'))
    planet_id = Column(Integer, ForeignKey('planeta.id'))
    character_id = Column(Integer, ForeignKey('personaje.id'))

    usuario = relationship(Usuario, back_populates='favoritos')
    planeta = relationship(Planeta)
    personaje = relationship(Personaje)

Usuario.favoritos = relationship(Favorito, back_populates='usuario')

render_er(Base, 'diagram.png')
