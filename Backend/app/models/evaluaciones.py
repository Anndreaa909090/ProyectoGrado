# app/models/evaluaciones.py
from sqlalchemy import Column, BigInteger, Integer, Float, TIMESTAMP, String, Text, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from app.database import Base

class EvaluacionLectura(Base):
    __tablename__ = "evaluacion_lectura"

    id = Column(BigInteger, primary_key=True)
    estudiante_id = Column(BigInteger, ForeignKey("estudiante.id", ondelete="CASCADE"), nullable=False)
    contenido_id = Column(BigInteger, ForeignKey("contenido_lectura.id", ondelete="CASCADE"), nullable=False)
    fecha_evaluacion = Column(TIMESTAMP(timezone=True))
    puntuacion_pronunciacion = Column(Float)
    velocidad_lectura = Column(Float)
    fluidez = Column(Float)
    precision_palabras = Column(Float)
    retroalimentacion_ia = Column(Text)
    audio_url = Column(String(500))
    duracion_audio = Column(Integer)
    estado = Column(String(20), default="completado")
    deleted_at = Column(TIMESTAMP(timezone=True))

    estudiante = relationship("Estudiante", back_populates="evaluaciones")
    contenido = relationship("ContenidoLectura", back_populates="evaluaciones")
    analisis = relationship("AnalisisIA", back_populates="evaluacion", uselist=False)
    intentos = relationship("IntentoLectura", back_populates="evaluacion")
    detalles = relationship("DetalleEvaluacion", back_populates="evaluacion")

class AnalisisIA(Base):
    __tablename__ = "analisis_ia"

    id = Column(BigInteger, primary_key=True)
    evaluacion_id = Column(BigInteger, ForeignKey("evaluacion_lectura.id", ondelete="CASCADE"), nullable=False)
    modelo_usado = Column(String(100))
    precision_global = Column(Float)
    palabras_detectadas = Column(JSONB)
    errores_detectados = Column(JSONB)
    tiempo_procesamiento = Column(Float)
    fecha_analisis = Column(TIMESTAMP(timezone=True))

    evaluacion = relationship("EvaluacionLectura", back_populates="analisis")

class IntentoLectura(Base):
    __tablename__ = "intento_lectura"

    id = Column(BigInteger, primary_key=True)
    evaluacion_id = Column(BigInteger, ForeignKey("evaluacion_lectura.id", ondelete="CASCADE"), nullable=False)
    numero_intento = Column(Integer, nullable=False)
    puntuacion_pronunciacion = Column(Float)
    velocidad_lectura = Column(Float)
    fluidez = Column(Float)
    audio_url = Column(String(500))
    fecha_intento = Column(TIMESTAMP(timezone=True))

    evaluacion = relationship("EvaluacionLectura", back_populates="intentos")

class DetalleEvaluacion(Base):
    __tablename__ = "detalle_evaluacion"

    id = Column(BigInteger, primary_key=True)
    evaluacion_id = Column(BigInteger, ForeignKey("evaluacion_lectura.id", ondelete="CASCADE"), nullable=False)
    palabra = Column(String(100), nullable=False)
    posicion_en_texto = Column(Integer, nullable=False)
    precision_pronunciacion = Column(Float)
    retroalimentacion_palabra = Column(String(300))
    timestamp_inicio = Column(Float)
    timestamp_fin = Column(Float)
    tipo_tokenizacion = Column(String(50))

    evaluacion = relationship("EvaluacionLectura", back_populates="detalles")
    errores = relationship("ErrorPronunciacion", back_populates="detalle")

class ErrorPronunciacion(Base):
    __tablename__ = "error_pronunciacion"

    id = Column(BigInteger, primary_key=True)
    detalle_evaluacion_id = Column(BigInteger, ForeignKey("detalle_evaluacion.id", ondelete="CASCADE"), nullable=False)
    tipo_error = Column(String(50), nullable=False)
    palabra_original = Column(String(100))
    palabra_detectada = Column(String(100))
    timestamp_inicio = Column(Float)
    timestamp_fin = Column(Float)
    severidad = Column(Integer)
    sugerencia_correccion = Column(Text)

    detalle = relationship("DetalleEvaluacion", back_populates="errores")
