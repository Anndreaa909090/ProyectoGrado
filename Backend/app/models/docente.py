# app/models/docente.py
from sqlalchemy import Column, BigInteger, String, Date, TIMESTAMP, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Docente(Base):
    __tablename__ = "docente"

    id = Column(BigInteger, primary_key=True)
    usuario_id = Column(BigInteger, ForeignKey("usuario.id", ondelete="CASCADE"), unique=True, nullable=False)
    especialidad = Column(String(100))
    grado_academico = Column(String(100))
    institucion = Column(String(200))
    fecha_contratacion = Column(Date)
    creado_en = Column(TIMESTAMP(timezone=True))
    activo = Column(Boolean, default=True)

    usuario = relationship("Usuario", back_populates="docente")
    cursos = relationship("Curso", back_populates="docente", cascade="all, delete-orphan")
    estudiantes = relationship("Estudiante", back_populates="docente")
    contenidos = relationship("ContenidoLectura", back_populates="docente")
