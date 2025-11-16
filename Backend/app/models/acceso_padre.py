from sqlalchemy import Column, BigInteger, String, TIMESTAMP, Boolean, ForeignKey, UniqueConstraint, Index
from sqlalchemy.sql import text as sql_text
from app.database import Base
from sqlalchemy.orm import relationship

class AccesoPadre(Base):
    __tablename__ = "acceso_padre"

    id = Column(BigInteger, primary_key=True)
    estudiante_id = Column(BigInteger, ForeignKey("estudiante.id", ondelete="CASCADE"), nullable=False)
    padre_id = Column(BigInteger, ForeignKey("padre.id", ondelete="SET NULL"))
    email_padre = Column(String(255))
    rol_padre = Column(String(50), default="padre")
    puede_ver_progreso = Column(Boolean, default=True)
    creado_en = Column(TIMESTAMP(timezone=True))

    estudiante = relationship("Estudiante", back_populates="accesos_padre")
    padre = relationship("Padre", back_populates="accesos")

    # Partial unique indexes created below (SQLAlchemy Index with postgresql_where)
    __table_args__ = (
        # note: we will create the Index objects below after class definition
        {}
    )

# Create partial unique indexes (padre_id not null) and (email_padre not null)
Index(
    "uniq_acceso_padre_por_id",
    AccesoPadre.estudiante_id,
    AccesoPadre.padre_id,
    unique=True,
    postgresql_where=sql_text("padre_id IS NOT NULL")
)
Index(
    "uniq_acceso_padre_por_email",
    AccesoPadre.estudiante_id,
    AccesoPadre.email_padre,
    unique=True,
    postgresql_where=sql_text("email_padre IS NOT NULL")
)
