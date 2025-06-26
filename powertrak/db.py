from sqlmodel import create_engine, Session, SQLModel

DATABASE_URL = "sqlite:///powertrak.db"
engine = create_engine(DATABASE_URL, echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session() -> Session:
    return Session(engine)
