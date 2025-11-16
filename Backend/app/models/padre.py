# app/models/padre.py
from sqlalchemy import Column, BigInteger, String, Boolean, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Padre(Base):
    __tablename__ = "padre"

    id = Column(BigInteger, primary_key=True)
    usuario_id = Column(BigInteger, ForeignKey("usuario.id", ondelete="SET NULL"), unique=True)
    telefono_contacto = Column(String(20))
    parentesco = Column(String(20))
    notificaciones_activas = Column(Boolean, default=True)
    creado_en = Column(TIMESTAMP(timezone=True))
    activo = Column(Boolean, default=True)
    deleted_at = Column(TIMESTAMP(timezone=True))

    usuario = relationship("Usuario", back_populates="padre")
    accesos = relationship("AccesoPadre", back_populates="padre")
