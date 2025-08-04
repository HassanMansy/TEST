# models1.py
from sqlalchemy import Table, Column, Integer, String, MetaData
from database1 import engine  # <-- make sure this import is correct

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String, nullable=False, unique=True),
    Column("password", String, nullable=False),
)

metadata.create_all(engine)  # <-- this should create the table
