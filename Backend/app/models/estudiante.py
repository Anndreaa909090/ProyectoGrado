# app/models/estudiante.py
from sqlalchemy import Column, BigInteger, String, Integer, Date, TIMESTAMP, Boolean, ForeignKey, JSON, Text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB
from app.database import Base
from sqlalchemy import Index, text

class Estudiante(Base):
    __tablename__ = "estudiante"

    id = Column(BigInteger, primary_key=True)
    usuario_id = Column(BigInteger, ForeignKey("usuario.id", ondelete="SET NULL"), unique=True)
    docente_id = Column(BigInteger, ForeignKey("docente.id", ondelete="CASCADE"), nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    nivel_educativo = Column(Integer, nullable=False)
    necesidades_especiales = Column(Text)
    avatar_url = Column(String(500))
    configuracion = Column(JSONB, default='{"sonidos": true, "animaciones": true, "dificultad": "media"}')
    creado_en = Column(TIMESTAMP(timezone=True))
    activo = Column(Boolean, default=True)
    deleted_at = Column(TIMESTAMP(timezone=True))
    transferible = Column(Boolean, default=True)

    usuario = relationship("Usuario")
    docente = relationship("Docente", back_populates="estudiantes")
    cursos = relationship("EstudianteCurso", back_populates="estudiante")
    accesos_padre = relationship("AccesoPadre", back_populates="estudiante")
    evaluaciones = relationship("EvaluacionLectura", back_populates="estudiante")
    nivel = relationship("NivelEstudiante", back_populates="estudiante", uselist=False)
