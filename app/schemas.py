from pydantic import BaseModel
from typing import Optional
from datetime import date, time
import enum
from decimal import Decimal

#Esquema de empleado
class EmpleadoBase(BaseModel):
    nombre : str
    apellido : str
    email : str
    telefono : str
    direccion : str
    puesto : str
    salario : Decimal
    
    class Config: 
         from_attributes = True
         
class Empleado(EmpleadoBase):
    id_empleado : int
    
    class Config: 
         from_attributes = True
         
#Esquema de proyecto
class ProyectoBase(BaseModel):
    nombre: str
    descripcion: str
    fecha_inicio: date
    fecha_fin: date
    porcentaje_completado: Decimal
    
    class Config:
        from_attributes = True
        
class Proyecto(ProyectoBase):
    id_proyecto: int
    
    class Config:
        from_attributes = True
        
class AsignacionBase(BaseModel):
    id_empleado: int
    id_proyecto: int
    fecha_asignacion: date
    
    class Config:
        from_attributes = True
        
class Asignacion(AsignacionBase):
    id_asignacion: int
    
    class Config:
        from_attributes = True 