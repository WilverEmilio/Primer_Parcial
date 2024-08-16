import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# DATABASE_URL = "mysql+mysqlconnector://root:EB163Q7E@localhost:3306/abarroteria" #Conectarse a la base de datos mediente contraseña
# DATABASE_URL = "mysql+mysqlconnector://root:@localhost:3306/abarroteria" #Conectarse a la base de datos sin contraseña
DATABASE_URL = "mysql+mysqlconnector://root:123456789@localhost:3306/recursos_humanos" #Conectarse a la base de datos mediente contraseña

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()