from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from server.config import db_config

DATABASE_URL = f"postgresql://{db_config.db_username}:{db_config.db_password}@{db_config.db_host}:{db_config.db_port}/{db_config.db_database}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
