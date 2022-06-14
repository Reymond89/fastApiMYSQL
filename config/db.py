from importlib import metadata
from django.template import Engine
from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:@localhost:3306/pruebadb")

meta = MetaData()

conn = engine.connect()