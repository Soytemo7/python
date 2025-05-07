#  pip install -r .\requirements.txt
# uvicorn main:app --reload
# https://render.com/docs/deploy-fastapi

from typing import List, Optional
import uuid
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# define modelo
class Curso(BaseModel):
    id:Optional[str]=None
    nombre:str
    description:Optional[str] = None
    nivel:str
    duracion:int

# simular base de datos

cursos_db = []

# CRUD: Read - GET

@app.get("/cursos/",response_model=List[Curso])
def obtener_cursos():
    return cursos_db

# CRUD Create - POST
@app.post("/cursos/",response_model=Curso)
def crear_curso(curso:Curso):
    curso.id = str(uuid.uuid4())
    cursos_db.append(curso)
    return curso    

# CRUD: Read - GET individual

@app.get("/cursos/{curso_id}",response_model=Curso)
def obtener_curso(curso_id:str):
    curso = next((curso for curso in cursos_db if curso.id == curso_id),None)       # next toma la primera coincidencia
    if curso is None:
        raise HTTPException(status_code=404,detail="Curso no encontrado")
    return curso

# CRUD: Actualizar - PUT

@app.put("/cursos/{curso_id}",response_model=Curso)
def actualizar_curso(curso_id:str,curso_actualizado:Curso):
    curso = next((curso for curso in cursos_db if curso.id == curso_id),None)       # next toma la primera coincidencia
    if curso is None:
        raise HTTPException(status_code=404,detail="Curso no encontrado")
    curso_actualizado.id = curso_id
    index = cursos_db.index(curso)
    cursos_db[index]=curso_actualizado
    return curso_actualizado


# CRUD: Borrado - DELETE

@app.delete("/cursos/{curso_id}",response_model=Curso)
def eliminar_curso(curso_id:str):
    curso = next((curso for curso in cursos_db if curso.id == curso_id),None)       # next toma la primera coincidencia
    if curso is None:
        raise HTTPException(status_code=404,detail="Curso no encontrado")
    cursos_db.remove(curso)
    return curso


