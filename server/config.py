from pydantic import BaseSettings

class DbConfig(BaseSettings):
    db_host: str
    db_port: int
    db_username: str
    db_password: str
    db_database: str

db_config = DbConfig()