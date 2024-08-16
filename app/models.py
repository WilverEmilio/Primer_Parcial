from sqlalchemy import Column, Integer, String, Date, Time, Enum, ForeignKey, Boolean
from sqlalchemy.types import DECIMAL
from sqlalchemy.orm import relationship
from .conexion import Base

#Modelo de empleados
class Empleados(Base):
    __tablename__ = 'empleados'
    id_empleado = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), index=True)
    apellido = Column(String(100), index=True)
    email = Column(String(100), index=True)
    telefono = Column(String(100), index=True)
    direccion = Column(String(100), index=True)
    puesto = Column(String(100), index=True)
    salario = Column(DECIMAL(10,2), index=True)
    
class Proyectos(Base):
    __tablename__ = 'proyectos'
    id_proyecto = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), index=True)
    descripcion = Column(String(100), index=True)
    fecha_inicio = Column(Date, index=True)
    fecha_fin = Column(Date, index=True)
    porcentaje_completado = Column(DECIMAL(5,2), index=True)
    
class Asignaciones(Base): 
    __tablename__ = 'asignaciones'
    id_asignacion = Column(Integer, primary_key=True, index=True)
    id_empleado = Column(Integer, ForeignKey('empleados.id_empleado'))
    id_proyecto = Column(Integer, ForeignKey('proyectos.id_proyecto'))
    fecha_asignacion = Column(Date, index=True)
    