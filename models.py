from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.sql.sqltypes import DateTime


Base = declarative_base()


stud_results = Table(
    "stud_results",
    Base.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column(
        "classes_id",
        Integer,
        ForeignKey("classes.id"),
        nullable=False,
    ),
    Column(
        "student_id",
        Integer,
        ForeignKey("students.id"),
        nullable=False,
    ),
    Column("mark", Integer, ForeignKey("marks.id"), nullable=False),
    Column("created_at", DateTime, default=datetime.now()),
)


class Marks(Base):
    __tablename__ = "marks"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column(Integer, nullable=False, unique=True)
    marks_relationship = relationship(stud_results)


class Groups(Base):
    __tablename__ = "groups"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column(String(10), nullable=False, unique=True)
    student = relationship("Students", secondary=stud_results, backref="groups")


class Students(Base):
    __tablename__ = "students"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)
    group_id = Column(Integer, ForeignKey("groups.id"))


class Teachers(Base):
    __tablename__ = "teachers"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)
    classes = relationship("Classes", secondary=stud_results, backref="teachers")


class Classes(Base):
    __tablename__ = "classes"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
