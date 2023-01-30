from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.sql.sqltypes import DateTime


Base = declarative_base()


class Groups(Base):
    __tablename__ = "groups"
    id = Column("id", Integer, primary_key=True)
    group_name = Column(String(10), nullable=False, unique=True)
    group_stud_relate = relationship(
        "Students", cascade="all, delete", backref="groups"
    )


class Students(Base):
    __tablename__ = "students"
    id = Column("id", Integer, primary_key=True)
    student = Column(String(255), nullable=False, unique=True)
    group_id = Column(String(50), ForeignKey("groups.id", ondelete="CASCADE"))


class Teachers(Base):
    __tablename__ = "teachers"
    id = Column("id", Integer, primary_key=True)
    teacher = Column(String(255), nullable=False, unique=True)
    teach_lesson_relate = relationship(
        "Classes", cascade="all, delete", backref="classes"
    )


class Classes(Base):
    __tablename__ = "classes"
    id = Column("id", Integer, primary_key=True)
    lesson = Column(String(255), nullable=False, unique=True)
    teacher_id = Column(String(50), ForeignKey("teachers.id", ondelete="CASCADE"))


marks = Table(
    "marks",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column(
        "lesson_id",
        ForeignKey("classes.id", ondelete="CASCADE"),
        Integer,
        nullable=False,
    ),
    Column(
        "student_id",
        ForeignKey("students.id", ondelete="CASCADE"),
        Integer,
        nullable=False,
    ),
    Column("mark", Integer, nullable=False),
    Column("created_at", DateTime, default=datetime.now()),
)
