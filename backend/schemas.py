from pydantic import BaseModel, Field, HttpUrl
from enum import Enum


class BreedEnum(str, Enum):
    golden_retriever = 'Golden Retriever'
    labrador_retriever = 'Labrador Retriever'
    poodle = 'Poodle'
    bulldog = 'Bulldog'
    australian_sheperd = 'Australian Sheperd'
    boxer = 'Boxer'
    rottweilers = 'Rottweiler'
    shih_tzu = 'Shih Tzu'

class Dog(BaseModel):
    name: str
    image_url: HttpUrl
    breed: BreedEnum