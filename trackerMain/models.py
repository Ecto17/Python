import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class custom(Base):
    __tablename__ = 'content'
    id = Column(Integer, primary_key=True)
    title = Column(String(80), nullable=False)
    development = Column(String(32), nullable=False)

engine = create_engine('sqlite:///sqlalchemy.db')

DBSession = sessionmaker(bind=engine)

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine