# app/models/auditoria.py
from sqlalchemy import Column, BigInteger, String, TIMESTAMP, Text, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB, INET
from sqlalchemy.orm import relationship
from app.database import Base
from sqlalchemy import Boolean


class Auditoria(Base):
    __tablename__ = "auditoria"

    id = Column(BigInteger, primary_key=True)
    usuario_id = Column(BigInteger, ForeignKey("usuario.id", ondelete="SET NULL"))
    accion = Column(String(100), nullable=False)
    tabla_afectada = Column(String(100))
    registro_id = Column(BigInteger)
    datos_anteriores = Column(JSONB)
    datos_nuevos = Column(JSONB)
    ip_address = Column(INET)
    user_agent = Column(Text)
    fecha_evento = Column(TIMESTAMP(timezone=True))

    usuario = relationship("Usuario", back_populates="auditorias")

class SesionUsuario(Base):
    __tablename__ = "sesion_usuario"

    id = Column(BigInteger, primary_key=True)
    usuario_id = Column(BigInteger, ForeignKey("usuario.id", ondelete="CASCADE"), nullable=False)
    token_sesion = Column(String(500), unique=True, nullable=False)
    fecha_inicio = Column(TIMESTAMP(timezone=True))
    fecha_expiracion = Column(TIMESTAMP(timezone=True))
    ip_address = Column(INET)
    dispositivo = Column(String(200))
    activa = Column(Boolean, default=True)

    usuario = relationship("Usuario", back_populates="sesiones")
