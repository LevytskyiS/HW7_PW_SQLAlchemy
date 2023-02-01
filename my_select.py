from connect_dp import session
from models import Grade, Student, Group, Teacher, Discipline
from sqlalchemy import func, desc


def select_1():

    results = (
        session.query(
            Student.fullname, func.round(func.avg(Grade.grade), 2).label("avg_grade")
        )
        .select_from(Grade)
        .join(Student)
        .group_by(Student.id)
        .order_by(desc("avg_grade"))
        .limit(5)
        .all()
    )

    return results


def select_2():

    results = (
        session.query(
            func.round(func.avg(Grade.grade), 2).label("avg_grade"),
            Discipline.name,
            Student.fullname,
        )
        .select_from(Grade)
        .join(Student)
        .join(Discipline)
        .group_by(Student.fullname, Discipline.name)
        .filter(Discipline.name == "Math")
        .order_by(desc("avg_grade"))
        .limit(1)
        .all()
    )

    return results


def select_3():

    results = (
        session.query(
            func.round(func.avg(Grade.grade), 2).label("avg_grade"),
            Group.name,
            Discipline.name,
        )
        .select_from(Grade)
        .join(Discipline)
        .join(Student)
        .join(Group)
        .group_by(Group.name, Discipline.name)
        .filter(
            Group.name == "xf-92",
            Discipline.name == "Math",
        )
        .all()
    )

    return results


def select_4():

    results = (
        session.query(func.round(func.avg(Grade.grade), 2).label("avg_grade"))
        .select_from(Grade)
        .order_by("avg_grade")
        .all()
    )

    return results


def select_5():

    results = (
        session.query(
            Teacher.fullname,
            Discipline.name,
        )
        .select_from(Discipline)
        .join(Teacher)
        .filter(Teacher.fullname == "Edward Arroyo")
        .all()
    )

    return results


def select_6():

    results = (
        session.query(
            Group.name,
            Student.fullname,
        )
        .select_from(Student)
        .join(Group)
        .filter(Group.name == "xf-92")
        .all()
    )

    return results


def select_7():

    results = (
        session.query(Group.name, Student.fullname, Grade.grade, Discipline.name)
        .select_from(Grade)
        .join(Student)
        .join(Group)
        .join(Discipline)
        .filter(
            Group.name == "xf-92",
            Discipline.name == "Math",
        )
        .order_by(Student.fullname)
        .all()
    )

    return results


def select_8():

    results = (
        session.query(
            func.round(func.avg(Grade.grade), 2).label("avg_grade"),
            Teacher.fullname,
        )
        .select_from(Grade)
        .join(Discipline)
        .join(Teacher)
        .filter(
            Teacher.fullname == "Edward Arroyo",
        )
        .group_by(Teacher.id)
        .all()
    )

    return results


def select_9():

    results = (
        session.query(Student.fullname, Discipline.name)
        .select_from(Grade)
        .join(Student)
        .join(Discipline)
        .filter(Student.fullname == "Christian Anderson")
        .all()
    )

    return results


def select_10():

    results = (
        session.query(Teacher.fullname, Student.fullname, Discipline.name)
        .select_from(Grade)
        .join(Discipline)
        .join(Student)
        .join(Teacher)
        .filter(
            Teacher.fullname == "Edward Arroyo",
            Student.fullname == "Christian Anderson",
        )
        .all()
    )

    return results
