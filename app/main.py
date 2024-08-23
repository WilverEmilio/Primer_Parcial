from typing import Annotated, List
from starlette.responses import RedirectResponse
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from . import crud
from .conexion import SessionLocal, engine
from .schemas import EmpleadoBase, ProyectoBase, AsignacionBase, Empleado, Proyecto, Asignacion
from .models import Base, Proyectos, Empleados
from datetime import datetime, timedelta
from fastapi.responses import JSONResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
#Ruta de inicio
@app.get('/')
def inicio():
    return RedirectResponse(url='/docs/')

#Rutas de empleados
@app.get('/empleadosObtener/', response_model=List[Empleado])
def empleados_obtener(db: Session = Depends(get_db)):
    empleados = crud.get_empleado(db)
    return empleados

@app.get('/empleadosObtener/{id_empleado}', response_model=Empleado)
def empleado_obtener(id_empleado: int, db: Session = Depends(get_db)):
    empleado = crud.get_empleado_by_id(db, id_empleado)
    if empleado is None:
        return empleado
    raise HTTPException(status_code=404, detail="El empleado con el id {id_empleado} no se encuentra en la base de datos")

@app.post('/empleadosCrear/', response_model=Empleado)
def empleado_crear(empleado: EmpleadoBase, db: Session = Depends(get_db)):
    return crud.create_empleado(db, empleado)

@app.put('/empleadosActualizar/{id_empleado}', response_model=Empleado)
def actualizar_empleado(id_empleado: int, empleado: EmpleadoBase, db: Session = Depends(get_db)):
    actualizar_empleado = crud.update_empleado(db, id_empleado, empleado=empleado)
    if actualizar_empleado is None:
        return actualizar_empleado
    raise HTTPException(status_code=404, detail="El empleado con el id {id_empleado} no se encuentra en la base de datos")

@app.delete('/empleadosEliminar/{id_empleado}', response_model=Empleado)
def eliminar_empleado(id_empleado: int, db: Session = Depends(get_db)):
    eliminar_empleado = crud.delete_empleado(db, id_empleado)
    if eliminar_empleado is None:
        return eliminar_empleado
    raise HTTPException(status_code=404, detail="El empleado con el id {id_empleado} no se encuentra en la base de datos")

#Rutas de proyectos
@app.get('/proyectosObtener/', response_model=List[Proyecto])
def proyectos_obtener(db: Session = Depends(get_db)):
    proyectos = crud.get_proyecto(db)
    return proyectos

@app.get('/proyectosObtener/{id_proyecto}', response_model=Proyecto)
def proyecto_obtener(id_proyecto: int, db: Session = Depends(get_db)):
    proyecto = crud.get_proyecto_by_id(db, id_proyecto)
    if proyecto is None:
        return proyecto
    raise HTTPException(status_code=404, detail="El proyecto con el id {id_proyecto} no se encuentra en la base de datos")

@app.post('/proyectosCrear/', response_model=Proyecto)
def proyecto_crear(proyecto: ProyectoBase, db: Session = Depends(get_db)):
    return crud.create_proyecto(db, proyecto)

@app.put('/proyectosActualizar/{id_proyecto}', response_model=Proyecto)
def actualizar_proyecto(id_proyecto: int, proyecto: ProyectoBase, db: Session = Depends(get_db)):
    actualizar_proyecto = crud.update_proyecto(db, id_proyecto, proyecto=proyecto)
    if actualizar_proyecto is None:
        return actualizar_proyecto
    raise HTTPException(status_code=404, detail="El proyecto con el id {id_proyecto} no se encuentra en la base de datos")

#Rutas de asignaciones
@app.get('/asignacionesObtener/', response_model=List[Asignacion])
def asignaciones_obtener(db: Session = Depends(get_db)):
    asignaciones = crud.get_asignacion(db)
    return asignaciones

@app.get('/asignacionesObtener/{id_asignacion}', response_model=Asignacion)
def asignacion_obtener(id_asignacion: int, db: Session = Depends(get_db)):
    asignacion = crud.get_asignacion_by_id(db, id_asignacion)
    if asignacion is None:
        return asignacion
    raise HTTPException(status_code=404, detail="La asignacion con el id {id_asignacion} no se encuentra en la base de datos")

@app.post('/asignacionesCrear/', response_model=Asignacion)
def asignacion_crear(asignacion: AsignacionBase, db: Session = Depends(get_db)):
    # Asegúrate de que Proyecto esté importado correctamente
    proyecto = db.query(Proyectos).filter(Proyectos.id_proyecto == asignacion.id_proyecto).first()
    
    if not proyecto:
        raise HTTPException(status_code=400, detail="El proyecto no existe")
    
    # Validar que la fecha de inicio del proyecto no sea mayor que la fecha de fin
    if proyecto.fecha_inicio > proyecto.fecha_fin:
        raise HTTPException(status_code=400, detail="La fecha de inicio del proyecto no puede ser mayor a la fecha de fin")
    
    # Verificar si el empleado existe
    empleado = db.query(Empleados).filter(Empleados.id_empleado == asignacion.id_empleado).first()
    if not empleado:
        raise HTTPException(status_code=400, detail="El empleado no existe")
    
    # Crear la asignación si todas las validaciones pasan
    return crud.create_asignacion(db, asignacion)


@app.get('/alertas/', response_model=List[Proyecto])
def obtener_proyectos_con_alerta(db: Session = Depends(get_db)):
    proyectos = crud.get_proyectos_con_alerta(db)
    return proyectos

