from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

user = "harshit"
password = "Harshit123#"
host = "127.0.0.1"
port = 3306
database = "fastapi"

DATABASE_URL = f"mysql+mysqldb://{user}:{password}@{host}:{port}/{database}"

db_engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

Base = declarative_base()


def get_db():
    """
    Method to generate db session
    :return: Session
    """
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()