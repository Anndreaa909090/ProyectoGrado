# app/models/contenido.py
from sqlalchemy import Column, BigInteger, String, Text, Integer, TIMESTAMP, Boolean, ForeignKey, ARRAY
from sqlalchemy.dialects.postgresql import JSONB, ARRAY as PG_ARRAY
from sqlalchemy.orm import relationship
from app.database import Base

class CategoriaLectura(Base):
    __tablename__ = "categoria_lectura"

    id = Column(BigInteger, primary_key=True)
    nombre = Column(String(200), nullable=False)
    descripcion = Column(Text)
    edad_minima = Column(Integer, nullable=False)
    edad_maxima = Column(Integer, nullable=False)
    color = Column(String(7), default="#3498db")
    icono = Column(String(100))
    activo = Column(Boolean, default=True)
    creado_en = Column(TIMESTAMP(timezone=True))
    deleted_at = Column(TIMESTAMP(timezone=True))

    contenidos = relationship("ContenidoLectura", back_populates="categoria")

class ContenidoLectura(Base):
    __tablename__ = "contenido_lectura"

    id = Column(BigInteger, primary_key=True)
    curso_id = Column(BigInteger, ForeignKey("curso.id", ondelete="SET NULL"))
    docente_id = Column(BigInteger, ForeignKey("docente.id", ondelete="SET NULL"))
    categoria_id = Column(BigInteger, ForeignKey("categoria_lectura.id", ondelete="SET NULL"))
    titulo = Column(String(300), nullable=False)
    contenido = Column(Text, nullable=False)
    audio_url = Column(String(500))
    duracion_audio = Column(Integer)
    nivel_dificultad = Column(Integer, nullable=False)
    edad_recomendada = Column(Integer, nullable=False)
    palabras_clave = Column(PG_ARRAY(String))
    etiquetas = Column(JSONB, default='[]')
    por_defecto = Column(Boolean, default=False)
    publico = Column(Boolean, default=False)
    fecha_creacion = Column(TIMESTAMP(timezone=True))
    fecha_actualizacion = Column(TIMESTAMP(timezone=True))
    activo = Column(Boolean, default=True)
    deleted_at = Column(TIMESTAMP(timezone=True))

    curso = relationship("Curso", back_populates="contenidos")
    docente = relationship("Docente", back_populates="contenidos")
    categoria = relationship("CategoriaLectura", back_populates="contenidos")
    actividades = relationship("Actividad", back_populates="contenido")
    evaluaciones = relationship("EvaluacionLectura", back_populates="contenido")
