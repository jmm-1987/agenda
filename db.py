from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

#Arraque para sqql PRUEBAS
#mysql_uri = 'mysql://dbu2682661:20%mn.-74Thkd5&el@db5015532831.hosting-data.io:3306/dbs12687167'
#Arraque para sqql
#engine = create_engine(mysql_uri)

#Arraque para Sqlite

engine = create_engine('sqlite:///database/AGENDA.db',
connect_args={'check_same_thread': False})


Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()