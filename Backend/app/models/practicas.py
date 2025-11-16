# app/models/practicas.py
from sqlalchemy import Column, BigInteger, Integer, Float, TIMESTAMP, String, Boolean,Text, ForeignKey
from sqlalchemy.dialects.postgresql import TEXT, JSONB, ARRAY
from sqlalchemy.orm import relationship
from app.database import Base

class EjercicioPractica(Base):
    __tablename__ = "ejercicio_practica"

    id = Column(BigInteger, primary_key=True)
    estudiante_id = Column(BigInteger, ForeignKey("estudiante.id", ondelete="CASCADE"), nullable=False)
    evaluacion_id = Column(BigInteger, ForeignKey("evaluacion_lectura.id", ondelete="CASCADE"), nullable=False)
    tipo_ejercicio = Column(String(50), nullable=False)
    palabras_objetivo = Column(ARRAY(String))
    texto_practica = Column(Text, nullable=False)
    dificultad = Column(Integer)
    completado = Column(Boolean, default=False)
    intentos = Column(Integer, default=0)
    fecha_creacion = Column(TIMESTAMP(timezone=True))
    fecha_completacion = Column(TIMESTAMP(timezone=True))
    deleted_at = Column(TIMESTAMP(timezone=True))

    estudiante = relationship("Estudiante")
    evaluacion = relationship("EvaluacionLectura")
    resultados = relationship("ResultadoEjercicio", back_populates="ejercicio")

class ResultadoEjercicio(Base):
    __tablename__ = "resultado_ejercicio"

    id = Column(BigInteger, primary_key=True)
    ejercicio_id = Column(BigInteger, ForeignKey("ejercicio_practica.id", ondelete="CASCADE"), nullable=False)
    puntuacion = Column(Float)
    audio_url = Column(String(500))
    retroalimentacion_ia = Column(Text)
    errores_corregidos = Column(Integer, default=0)
    tiempo_practica = Column(Integer)
    fecha_completacion = Column(TIMESTAMP(timezone=True))

    ejercicio = relationship("EjercicioPractica", back_populates="resultados")
