# ==========================================
# db.py  ->  Connection to the database
# ==========================================
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base

# MySQL server address. Format: mysql+pymysql://USERNAME:PASSWORD@HOST:PORT
# XAMPP: username is root and the password is empty
# SERVER_URL = "mysql+pymysql://root:@localhost:3306"
# DB_NAME = "alchemyBD"
#
# # Create the database automatically if it doesn't exist yet
# # (so you don't need phpMyAdmin to create it)
# try:
#     with create_engine(SERVER_URL).connect() as connection:
#         connection.execute(text(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"))
# except Exception as error:
#     print("\n" + "=" * 60)
#     print(" ERROR: Could not connect to MySQL!")
#     print(" 1. Open XAMPP and click Start next to MySQL")
#     print(" 2. Check the username / password in SERVER_URL (db.py)")
#     print(" Details:", error)
#     print("=" * 60 + "\n")
#     raise SystemExit(1)

# Full address of our database
# DATABASE_URL = f"{SERVER_URL}/{DB_NAME}"
#DATABASE_URL = "postgresql+psycopg2://training_kw7c_user:M61kuqHG8f1nJcaA7AOtuqM1PHYbSc5B@dpg-dc36gf3rjlhs73eutr0g-a.oregon-postgres.render.com/training_kw7c"
#DATABASE_URL = "postgresql+psycopg2://fastapi001_user:qWRihJALUJClAYqWbViFibtn3LKRXbny@dpg-dc387vhksfps739bj7l0-a.virginia-postgres.render.com/fastapi001"
DATABASE_URL = "postgresql+psycopg2://zilani_user:KPQnA7NN8qpEQGK6RiabyQJJRS9cwnNz@dpg-dc4ob30u01pc73epsslg-a.virginia-postgres.render.com/zilani"
engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
base = declarative_base()


# Opens a database session for each request
# and closes it when the work is done.
# Used in routers like this:  db: Session = Depends(get_db)
def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
