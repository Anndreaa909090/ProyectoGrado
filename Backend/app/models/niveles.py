# app/models/niveles.py
from sqlalchemy import Column, BigInteger, Integer, TIMESTAMP, Boolean, String,Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from sqlalchemy import Date


class NivelEstudiante(Base):
    __tablename__ = "nivel_estudiante"

    id = Column(BigInteger, primary_key=True)
    estudiante_id = Column(BigInteger, ForeignKey("estudiante.id", ondelete="CASCADE"), unique=True, nullable=False)
    nivel_actual = Column(Integer, default=1)
    puntos_totales = Column(Integer, default=0)
    puntos_nivel_actual = Column(Integer, default=0)
    puntos_para_siguiente_nivel = Column(Integer, default=1000)
    lecturas_completadas = Column(Integer, default=0)
    actividades_completadas = Column(Integer, default=0)
    racha_actual = Column(Integer, default=0)
    racha_maxima = Column(Integer, default=0)
    fecha_actualizacion = Column(TIMESTAMP(timezone=True))

    estudiante = relationship("Estudiante", back_populates="nivel")

class Recompensa(Base):
    __tablename__ = "recompensa"

    id = Column(BigInteger, primary_key=True)
    nombre = Column(String(200), nullable=False)
    descripcion = Column(Text)
    tipo = Column(String(50), nullable=False)
    puntos_requeridos = Column(Integer)
    nivel_requerido = Column(Integer)
    lectura_id = Column(BigInteger, ForeignKey("contenido_lectura.id", ondelete="SET NULL"))
    imagen_url = Column(String(500))
    rareza = Column(String(20), default="comun")
    activo = Column(Boolean, default=True)
    fecha_creacion = Column(TIMESTAMP(timezone=True))

    recompensas_estudiantes = relationship("RecompensaEstudiante", back_populates="recompensa")

class RecompensaEstudiante(Base):
    __tablename__ = "recompensa_estudiante"

    id = Column(BigInteger, primary_key=True)
    estudiante_id = Column(BigInteger, ForeignKey("estudiante.id", ondelete="CASCADE"), nullable=False)
    recompensa_id = Column(BigInteger, ForeignKey("recompensa.id", ondelete="CASCADE"), nullable=False)
    fecha_obtencion = Column(TIMESTAMP(timezone=True))
    visto = Column(Boolean, default=False)

    recompensa = relationship("Recompensa", back_populates="recompensas_estudiantes")

class MisionDiaria(Base):
    __tablename__ = "mision_diaria"

    id = Column(BigInteger, primary_key=True)
    estudiante_id = Column(BigInteger, ForeignKey("estudiante.id", ondelete="CASCADE"), nullable=False)
    tipo_mision = Column(String(100))
    objetivo = Column(Integer)
    progreso = Column(Integer, default=0)
    completada = Column(Boolean, default=False)
    recompensa_puntos = Column(Integer, default=50)
    fecha = Column(Date)

class HistorialPuntos(Base):
    __tablename__ = "historial_puntos"

    id = Column(BigInteger, primary_key=True)
    estudiante_id = Column(BigInteger, ForeignKey("estudiante.id", ondelete="CASCADE"), nullable=False)
    motivo = Column(String(200))
    puntos = Column(Integer)
    fecha = Column(TIMESTAMP(timezone=True))
