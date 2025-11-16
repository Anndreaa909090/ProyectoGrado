# app/models/__init__.py
from .usuario import Usuario, ContrasenaAnterior, UsuarioRol
from .docente import Docente
from .padre import Padre
from .estudiante import Estudiante, AccesoPadre
from .curso import Curso, EstudianteCurso
from .contenido import CategoriaLectura, ContenidoLectura
from .evaluaciones import EvaluacionLectura, AnalisisIA, IntentoLectura, DetalleEvaluacion, ErrorPronunciacion
from .practicas import EjercicioPractica, ResultadoEjercicio
from .actividades import Actividad, Pregunta, ProgresoActividad, RespuestaPregunta
from .niveles import NivelEstudiante, Recompensa, RecompensaEstudiante, MisionDiaria, HistorialPuntos
from .auditoria import Auditoria, SesionUsuario
