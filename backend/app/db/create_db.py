import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from app.core.config import settings

def create_database():
    # Connect to default postgres DB
    conn = psycopg2.connect(
        dbname="postgres",
        user=settings.db_user,
        password=settings.db_password,
        host=settings.db_host,
        port=settings.db_port
    )
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    cur = conn.cursor()

    # Check if database exists
    cur.execute(f"SELECT 1 FROM pg_database WHERE datname='{settings.db_name}';")
    exists = cur.fetchone()
    if not exists:
        cur.execute(f"CREATE DATABASE {settings.db_name};")
        print(f"Database {settings.db_name} created.")
    else:
        print(f"Database {settings.db_name} already exists.")

    cur.close()
    conn.close()

if __name__ == "__main__":
    create_database()