# powertrak/database.py

from sqlmodel import SQLModel, create_engine, Session
from powertrak.config import config

engine = create_engine(config.db_url, echo=config.debug)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    return Session(engine)
