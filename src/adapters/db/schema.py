
from sqlalchemy import (
    Boolean,
    Column,
    Integer,
    String,
    Text
)
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import (
    declarative_base,
    sessionmaker
)

SQLALCHEMY_DATABASE_URL = "sqlite:///./todoApp.db"

Base = declarative_base()

class DBSession:
    def __init__(self) -> None:
        self.engine = create_engine(
            SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
        )
        self.Session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    @contextmanager
    def get_db(self):
        session = self.Session()
        try:
            yield session
        finally:
            session.close()

class TodoTable(Base):
    __tablename__ = "todos"

    id = Column(Text, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    is_completed = Column(Boolean, default=False)
