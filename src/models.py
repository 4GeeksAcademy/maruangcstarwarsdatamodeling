import os
import sys
import datetime
import enum
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# Para que el campo category en favorite solo tenga estos 3 valores posibles
# No se usara para que el diagrama se dibuje con las relaciones
# Pero se deja para referencia y nota personal
class Category(enum.Enum):
    starship = 'starship'
    character = 'character'
    planet = 'planet'

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(300), unique=False, nullable=False)
    name = Column(String(250), unique=False, nullable=False)
    date_subscripcion = Column(DateTime, unique=False)

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'))
    # el campo category se enlaza con la clase Category para  forzar 3 valores posibles
    # category = Column(Enum(Category), nullable=False)
    character_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    starship_id = Column(Integer, ForeignKey('starship.id'))
    person = relationship(Person)
    character = relationship('Character')
    planet = relationship('Planet')
    Starship = relationship('Starship')

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=False, nullable=False)
    height = Column(Integer, unique=False)
    mass = Column(Integer, unique=False)
    hair_color = Column(String(20), unique=False)
    skin_color = Column(String(20), unique=False)
    birth_year = Column(String(20), unique=False)
    gender = Column(String(20), unique=False)
    created = Column(DateTime, unique=False)
    edited = Column(DateTime, unique=False)
    homeworld = Column(String(200), unique=False)
    favorite = relationship(Favorite)
    pilot = relationship('Pilot')

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=False, nullable=False)
    diameter = Column(Integer, unique=False)
    rotation_period = Column(Integer, unique=False)
    orbital_period = Column(Integer, unique=False)
    gravity = Column(String(50), unique=False)
    population = Column(Integer, unique=False)
    climate = Column(String(50), unique=False)
    terrain = Column(String(50), unique=False)
    surface_water = Column(Integer, unique=False)
    created = Column(DateTime, unique=False)
    edited = Column(DateTime, unique=False)
    favorite = relationship(Favorite)

class Starship(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=False, nullable=False)
    model = Column(String(100), unique=False)
    starship_class = Column(String(100), unique=False)
    manufacturer = Column(String(100), unique=False)
    cost_in_credits = Column(Integer, unique=False)
    length = Column(Integer, unique=False)
    crew = Column(Integer, unique=False)
    passengers = Column(Integer, unique=False)
    max_atmosphering_speed = Column(String(50), unique=False)
    hyperdrive_rating = Column(String(20), unique=False)
    mglt = Column(Integer, unique=False)
    cargo_capacity = Column(Integer, unique=False)
    consumables = Column(String(50), unique=False)
    created = Column(DateTime, unique=False)
    edited = Column(DateTime, unique=False)
    favorite = relationship(Favorite)
    pilot = relationship('Pilot')

class Pilot(Base):
    __tablename__ = 'pilot'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'))
    starship_id = Column(Integer, ForeignKey('starship.id'))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
