from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from passlib.hash import bcrypt
from ..database import get_db
from .. import models, schemas

router = APIRouter(prefix="/docentes", tags=["Docentes"])


@router.post("/", response_model=schemas.DocenteResponse)
def crear_docente(data: schemas.DocenteCreate, db: Session = Depends(get_db)):
    existe = db.query(models.Docente).filter(models.Docente.email == data.email).first()
    if existe:
        raise HTTPException(status_code=400, detail="El correo ya está registrado.")

    docente = models.Docente(
        nombre=data.nombre,
        email=data.email,
        escuela=data.escuela,
        password_hash=bcrypt.hash(data.password)
    )

    db.add(docente)
    db.commit()
    db.refresh(docente)

    return docente
