from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schemas import Dog
from fastapi.middleware.cors import CORSMiddleware
from typing import List

origins = [
    'http://localhost:3000'
]

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=['*'], allow_headers=['*'])

dogs = []


@app.get('/api/dog/')
def root() -> List[Dog]:
    return [{
        'id': dogs.index(dog) + 1,
        'name': dog.name,
        'image_url': dog.image_url,
        'breed': dog.breed
    } for dog in dogs]

@app.post('/api/dog/')
def add_dog(dog: Dog) -> Dog:
    dogs.append(dog)
    return dog

@app.delete('/api/dog/{dog_id}/')
def add_dog(dog_id: int):
    try:
        del dogs[dog_id - 1]
    except:
        return JSONResponse(status_code=404, content={"message": "Dog not found"})
    return {'ok': True}