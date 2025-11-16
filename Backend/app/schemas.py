from pydantic import BaseModel


class DocenteCreate(BaseModel):
    nombre: str
    email: str
    password: str
    escuela: str | None = None


class DocenteResponse(BaseModel):
    id: int
    nombre: str
    email: str
    escuela: str | None

    class Config:
        orm_mode = True


class EstudianteCreate(BaseModel):
    docente_id: int
    nombre: str
    apellido: str
    grado: str
    email: str | None = None
    username: str
    password: str


class PadreCreate(BaseModel):
    estudiante_id: int
    nombre: str
    email: str | None = None
    telefono: str | None = None
    username: str
    password: str
