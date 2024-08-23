from sqlalchemy.orm import Session
from .models import Empleados, Proyectos, Asignaciones
from .schemas import EmpleadoBase, ProyectoBase, AsignacionBase
from datetime import datetime, timedelta

#CRUD de empleados
def get_empleado(db: Session):
    return db.query(Empleados).all()

def get_empleado_by_id(db: Session, id_empleado: int):
    return db.query(Empleados).filter(Empleados.id_empleado == id_empleado).first()

def create_empleado(db: Session, empleado: EmpleadoBase):
    new_empleado = Empleados(empleado=empleado.nombre, apellido=empleado.apellido, email=empleado.email, telefono=empleado.telefono, direccion=empleado.direccion, puesto=empleado.puesto, salario=empleado.salario)
    db.add(new_empleado)
    db.commit()
    db.refresh(new_empleado)
    return new_empleado

def create_empleado(db: Session, empleado: EmpleadoBase):
    new_empleado = Empleados(
        nombre=empleado.nombre,
        apellido=empleado.apellido,
        email=empleado.email,
        telefono=empleado.telefono,
        direccion=empleado.direccion,
        puesto=empleado.puesto,
        salario=empleado.salario
    )
    db.add(new_empleado)
    db.commit()
    db.refresh(new_empleado)
    return new_empleado


def delete_empleado(db: Session, id_empleado: int):
    db_empleado = db.query(Empleados).filter(Empleados.id_empleado == id_empleado).first()
    if db_empleado:
        db.delete(db_empleado)
        db.commit()
    return db_empleado

#CRUD de proyectos
def get_proyecto(db: Session):
    return db.query(Proyectos).all()

def get_proyecto_by_id(db: Session, id_proyecto: int):
    return db.query(Proyectos).filter(Proyectos.id_proyecto == id_proyecto).first()

def create_proyecto(db: Session, proyecto: ProyectoBase):
    new_proyecto = Proyectos(nombre=proyecto.nombre, descripcion=proyecto.descripcion, fecha_inicio=proyecto.fecha_inicio, fecha_fin=proyecto.fecha_fin, porcentaje_completado=proyecto.porcentaje_completado)
    db.add(new_proyecto)
    db.commit()
    db.refresh(new_proyecto)
    return new_proyecto

def update_proyecto(db: Session, id_proyecto: int, proyecto: ProyectoBase):
    db_proyecto = db.query(Proyectos).filter(Proyectos.id_proyecto == id_proyecto).first()
    if db_proyecto:
        db_proyecto.nombre = proyecto.nombre
        db_proyecto.descripcion = proyecto.descripcion
        db_proyecto.fecha_inicio = proyecto.fecha_inicio
        db_proyecto.fecha_fin = proyecto.fecha_fin
        db_proyecto.porcentaje_completado = proyecto.porcentaje_completado
        db.commit()
        db.refresh(db_proyecto)
    return db_proyecto

def delete_proyecto(db: Session, id_proyecto: int):
    db_proyecto = db.query(Proyectos).filter(Proyectos.id_proyecto == id_proyecto).first()
    if db_proyecto:
        db.delete(db_proyecto)
        db.commit()
    return db_proyecto

#CRUD de asignaciones
def get_asignacion(db: Session):
    return db.query(Asignaciones).all()

def get_asignacion_by_id(db: Session, id_asignacion: int):
    return db.query(Asignaciones).filter(Asignaciones.id_asignacion == id_asignacion).first()

def create_asignacion(db: Session, asignacion: AsignacionBase):
    new_asignacion = Asignaciones(id_empleado=asignacion.id_empleado, id_proyecto=asignacion.id_proyecto, fecha_asignacion=asignacion.fecha_asignacion)
    db.add(new_asignacion)
    db.commit()
    db.refresh(new_asignacion)
    return new_asignacion

def update_asignacion(db: Session, id_asignacion: int, asignacion: AsignacionBase):
    db_asignacion = db.query(Asignaciones).filter(Asignaciones.id_asignacion == id_asignacion).first()
    if db_asignacion:
        db_asignacion.id_empleado = asignacion.id_empleado
        db_asignacion.id_proyecto = asignacion.id_proyecto
        db_asignacion.fecha_asignacion = asignacion.fecha_asignacion
        db.commit()
        db.refresh(db_asignacion)
    return db_asignacion

def delete_asignacion(db: Session, id_asignacion: int):
    db_asignacion = db.query(Asignaciones).filter(Asignaciones.id_asignacion == id_asignacion).first()
    if db_asignacion:
        db.delete(db_asignacion)
        db.commit()
    return db_asignacion

def get_proyectos_con_alerta(db: Session):
    # Calcula la fecha límite para las alertas
    fecha_actual = datetime.now().date()
    fecha_limite = fecha_actual + timedelta(days=7)
    
    print(f"Fecha actual: {fecha_actual}")
    print(f"Fecha límite: {fecha_limite}")  
    
    # Filtra los proyectos que están dentro del rango de alerta
    proyectos = db.query(Proyectos).filter(Proyectos.fecha_fin <= fecha_limite, Proyectos.fecha_fin >= fecha_actual).all()
    
    print(f"Proyectos encontrados: {proyectos}")
    
    return proyectos