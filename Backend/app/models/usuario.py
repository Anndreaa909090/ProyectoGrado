# app/models/usuario.py
from sqlalchemy import Column, BigInteger, String, Boolean, Integer, TIMESTAMP, Text, Index
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB
from app.database import Base

class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(BigInteger, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    fecha_creacion = Column(TIMESTAMP(timezone=True), server_default="CURRENT_TIMESTAMP")
    activo = Column(Boolean, default=True)
    ultimo_login = Column(TIMESTAMP(timezone=True))
    intentos_login = Column(Integer, default=0)
    bloqueado = Column(Boolean, default=False)
    fecha_actualizacion = Column(TIMESTAMP(timezone=True))
    deleted_at = Column(TIMESTAMP(timezone=True))
    otp_secret = Column(String(255))
    otp_habilitado = Column(Boolean, default=False)

    # relationships
    roles = relationship("UsuarioRol", back_populates="usuario", cascade="all, delete-orphan")
    docente = relationship("Docente", back_populates="usuario", uselist=False)
    padre = relationship("Padre", back_populates="usuario", uselist=False)
    # possible user->sesiones
    sesiones = relationship("SesionUsuario", back_populates="usuario", cascade="all, delete-orphan")
    auditorias = relationship("Auditoria", back_populates="usuario")

class ContrasenaAnterior(Base):
    __tablename__ = "contrasena_anterior"

    id = Column(BigInteger, primary_key=True)
    usuario_id = Column(BigInteger, nullable=False)
    password_hash_old = Column(String(255), nullable=False)
    fecha_cambio = Column(TIMESTAMP(timezone=True))

    # ForeignKey set via relationships in other modules to avoid circular import

class UsuarioRol(Base):
    __tablename__ = "usuario_rol"

    id = Column(BigInteger, primary_key=True)
    usuario_id = Column(BigInteger, nullable=False)
    rol = Column(String(50), nullable=False)
    fecha_asignacion = Column(TIMESTAMP(timezone=True))
    fecha_expiracion = Column(TIMESTAMP(timezone=True))
    activo = Column(Boolean, default=True)

    # relationships
    usuario = relationship("Usuario", back_populates="roles")
