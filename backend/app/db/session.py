from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker
from core.config import settings

SQLALCHEMY_DATABASE_URL = URL.create(
    "postgresql+psycopg2",
    username=settings.db_user,
    password=settings.db_password,
    host=settings.db_password,
    port=settings.db_port,
    database=settings.db_name,
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()