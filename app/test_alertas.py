from datetime import datetime, timedelta
from app import crud 
from app.crud import get_proyectos_con_alerta
from .schemas import ProyectoBase
from sqlalchemy.orm import Session

def test_get_proyectos_con_alerta(db: Session):
    # Crear un proyecto con fecha de entrega en 3 días
    proyecto = ProyectoBase(
        nombre="Proyecto Test",
        descripcion="Descripción de prueba",
        fecha_inicio=datetime.now().date(),
        fecha_fin=datetime.now().date() + timedelta(days=3),
        porcentaje_completado=50
    )
    db_proyecto = crud.create_proyecto(db, proyecto)
    
    # Llamar a la función que debe devolver este proyecto
    proyectos_alerta = get_proyectos_con_alerta(db)
    
    assert len(proyectos_alerta) == 1
    assert proyectos_alerta[0].id_proyecto == db_proyecto.id_proyecto
