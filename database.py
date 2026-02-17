from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from urllib.parse import quote_plus



# SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"


password = quote_plus("Alliswell@1")

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://maniraj:{password}@localhost:3306/geeksblogs"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


def get_db():
    with SessionLocal() as db:
        yield db