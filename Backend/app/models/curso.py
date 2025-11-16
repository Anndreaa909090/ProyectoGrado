# app/models/cursos.py
from sqlalchemy import Column, BigInteger, String, Integer, TIMESTAMP, Boolean, ForeignKey, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB
from app.database import Base

class Curso(Base):
    __tablename__ = "curso"

    id = Column(BigInteger, primary_key=True)
    docente_id = Column(BigInteger, ForeignKey("docente.id", ondelete="CASCADE"), nullable=False)
    nombre = Column(String(200), nullable=False)
    descripcion = Column(String)
    nivel = Column(Integer, nullable=False)
    codigo_acceso = Column(String(50), unique=True)
    fecha_creacion = Column(TIMESTAMP(timezone=True))
    activo = Column(Boolean, default=True)
    configuracion = Column(JSONB, default='{"max_estudiantes": 30, "publico": false}')
    deleted_at = Column(TIMESTAMP(timezone=True))

    docente = relationship("Docente", back_populates="cursos")
    estudiantes = relationship("EstudianteCurso", back_populates="curso")
    contenidos = relationship("ContenidoLectura", back_populates="curso")

class EstudianteCurso(Base):
    __tablename__ = "estudiante_curso"

    id = Column(BigInteger, primary_key=True)
    estudiante_id = Column(BigInteger, ForeignKey("estudiante.id", ondelete="CASCADE"), nullable=False)
    curso_id = Column(BigInteger, ForeignKey("curso.id", ondelete="CASCADE"), nullable=False)
    fecha_inscripcion = Column(TIMESTAMP(timezone=True))
    estado = Column(String(20), default="activo")

    estudiante = relationship("Estudiante", back_populates="cursos")
    curso = relationship("Curso", back_populates="estudiantes")
