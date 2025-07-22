from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Candidate(Base):
    __tablename__ = 'candidates'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    resume_text = Column(Text, nullable=False)
    skills = Column(Text, nullable=True)
    experience = Column(Text, nullable=True)

    def __repr__(self):
        return f"<Candidate(name={self.name}, email={self.email})>"

class JobDescription(Base):
    __tablename__ = 'job_descriptions'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description_text = Column(Text, nullable=False)

    def __repr__(self):
        return f"<JobDescription(title={self.title})>"