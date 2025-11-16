# app/models/actividades.py
from sqlalchemy import Column, BigInteger, String, Text, Integer, TIMESTAMP, Float,Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from app.database import Base

class Actividad(Base):
    __tablename__ = "actividad"

    id = Column(BigInteger, primary_key=True)
    contenido_id = Column(BigInteger, ForeignKey("contenido_lectura.id", ondelete="CASCADE"), nullable=False)
    tipo = Column(String(50), nullable=False)
    titulo = Column(String(200), nullable=False)
    descripcion = Column(Text)
    configuracion = Column(JSONB, nullable=False)
    puntos_maximos = Column(Integer, nullable=False)
    tiempo_estimado = Column(Integer)
    dificultad = Column(Integer)
    activo = Column(Boolean, default=True)
    fecha_creacion = Column(TIMESTAMP(timezone=True))
    deleted_at = Column(TIMESTAMP(timezone=True))

    contenido = relationship("ContenidoLectura", back_populates="actividades")
    preguntas = relationship("Pregunta", back_populates="actividad")
    progresos = relationship("ProgresoActividad", back_populates="actividad")

class Pregunta(Base):
    __tablename__ = "pregunta"

    id = Column(BigInteger, primary_key=True)
    actividad_id = Column(BigInteger, ForeignKey("actividad.id", ondelete="CASCADE"), nullable=False)
    texto_pregunta = Column(Text, nullable=False)
    tipo_respuesta = Column(String(50), nullable=False)
    opciones = Column(JSONB)
    respuesta_correcta = Column(Text)
    puntuacion = Column(Integer, nullable=False)
    explicacion = Column(Text)
    orden = Column(Integer, default=1)

    actividad = relationship("Actividad", back_populates="preguntas")

class ProgresoActividad(Base):
    __tablename__ = "progreso_actividad"

    id = Column(BigInteger, primary_key=True)
    estudiante_id = Column(BigInteger, ForeignKey("estudiante.id", ondelete="CASCADE"), nullable=False)
    actividad_id = Column(BigInteger, ForeignKey("actividad.id", ondelete="CASCADE"), nullable=False)
    puntuacion = Column(Float, nullable=False)
    fecha_completacion = Column(TIMESTAMP(timezone=True))
    intentos = Column(Integer, default=1)
    tiempo_completacion = Column(Integer)
    errores_cometidos = Column(Integer, default=0)
    respuestas = Column(JSONB)
    deleted_at = Column(TIMESTAMP(timezone=True))

    estudiante = relationship("Estudiante")
    actividad = relationship("Actividad", back_populates="progresos")
    respuestas_individuales = relationship("RespuestaPregunta", back_populates="progreso")

class RespuestaPregunta(Base):
    __tablename__ = "respuesta_pregunta"

    id = Column(BigInteger, primary_key=True)
    progreso_id = Column(BigInteger, ForeignKey("progreso_actividad.id", ondelete="CASCADE"), nullable=False)
    pregunta_id = Column(BigInteger, ForeignKey("pregunta.id", ondelete="CASCADE"), nullable=False)
    respuesta_estudiante = Column(Text)
    correcta = Column(Boolean)
    puntuacion_obtenida = Column(Integer)
    tiempo_respuesta = Column(Integer)

    progreso = relationship("ProgresoActividad", back_populates="respuestas_individuales")
    pregunta = relationship("Pregunta")
