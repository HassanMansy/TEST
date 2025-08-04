from sqlalchemy import create_engine, MetaData

# Update your credentials here
DATABASE_URL = "postgresql://postgres:12345@localhost/suna?sslmode=disable"

engine = create_engine(DATABASE_URL)
metadata = MetaData()
