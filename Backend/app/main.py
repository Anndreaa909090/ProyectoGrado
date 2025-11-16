# app/main.py

from fastapi import FastAPI
from sqlalchemy import text
from app.database import engine
import time

app = FastAPI(title="API Proyecto Tutor")



@app.get("/test-db")
def test_db_connection():
    """Prueba la conexión a PostgreSQL"""
    try:
        # Intenta una conexión rápida con timeout
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1 as test_value"))
            row = result.fetchone()
            
            return {
                "status": "success", 
                "message": "✅ Conexión a PostgreSQL exitosa!",
                "database_test": row._asdict(),
                "database": "PostgreSQL"
            }
    except Exception as e:
        return {
            "status": "error",
            "message": "❌ Error conectando a PostgreSQL",
            "error_details": str(e),
            "solution": "Verifica que PostgreSQL esté ejecutándose en localhost:5432"
        }

@app.get("/db-info")
def get_db_info():
    """Obtiene información básica de la base de datos"""
    try:
        with engine.connect() as connection:
            db_name = connection.execute(text("SELECT current_database()")).scalar()
            db_user = connection.execute(text("SELECT current_user")).scalar()
            db_time = connection.execute(text("SELECT NOW()")).scalar()
            
            return {
                "status": "success",
                "database_name": db_name,
                "database_user": db_user,
                "server_time": str(db_time),
                "connection": "PostgreSQL"
            }
    except Exception as e:
        return {
            "status": "error", 
            "message": "No se pudo obtener información de la BD",
            "error": str(e)
        }