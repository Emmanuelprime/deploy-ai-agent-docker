import os
import sqlmodel
from sqlmodel import Session,SQLModel

DATABASE_URI = os.environ.get("DATABASE_URI")

if DATABASE_URI == "":
    raise NotImplementedError("DATABASE_URI needs to be given")

engine = sqlmodel.create_engine(DATABASE_URI)

#database models

def init_db():
    print("Creating database tables...")
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
