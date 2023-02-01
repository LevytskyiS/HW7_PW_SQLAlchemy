import faker
from datetime import datetime
from connect_dp import session
from models import Grade, Student, Group, Teacher, Discipline
from random import randint, choice


NUMBER_OF_STUDENTS = 30
NUMBER_OF_TEACHERS = 3
NUMBER_OF_CLASSES = 7
NUMBER_OF_GROUPS = 3


def generate_data(number_studs, number_teachers, number_groups) -> tuple:

    fake_students = []
    fake_teachers = []
    fake_classes = [
        "Math",
        "History",
        "Arts",
        "Literature",
        "Biology",
        "Algebra",
        "Chemistry ",
    ]
    fake_groups = []
    fake_marks = [1, 2, 3, 4, 5]
    fake_data = faker.Faker()

    for _ in range(number_studs):
        fake_students.append(fake_data.name())

    for _ in range(number_teachers):
        fake_teachers.append(fake_data.name())

    for _ in range(number_groups):
        fake_groups.append(fake_data.bothify(text="??-##"))

    return fake_students, fake_teachers, fake_classes, fake_groups, fake_marks


def prepare_data(students, teachers, classes, groups, marks) -> tuple:

    for_students = []
    for student in students:
        for_students.append((student, randint(1, NUMBER_OF_GROUPS)))

    for_teachers = []
    for teacher in teachers:
        for_teachers.append((teacher,))

    for_classes = []
    for lesson in classes:
        for_classes.append((lesson, randint(1, NUMBER_OF_TEACHERS)))

    for_groups = []
    for one_group in groups:
        for_groups.append((one_group,))

    for_marks = marks

    for_common_table = []
    for student in students:
        for _ in range(5):
            mark_date = datetime(2022, randint(1, 12), randint(1, 28)).date()
            for_common_table.append(
                (
                    randint(1, NUMBER_OF_CLASSES),
                    students.index(student) + 1,
                    choice(for_marks),
                    mark_date,
                )
            )

    return (
        for_students,
        for_teachers,
        for_classes,
        for_groups,
        for_marks,
        for_common_table,
    )


def insert_data_to_db(students, teachers, classes, groups, mark, final_table) -> None:

    for_groups = []
    for group in groups:
        for_groups.append(Group(name=group[0]))

    session.add_all(for_groups)
    session.commit()

    for_students = []
    for student in students:
        for_students.append(Student(fullname=student[0], group_id=student[1]))

    session.add_all(for_students)
    session.commit()

    for_teachers = []
    for teacher in teachers:
        for_teachers.append(Teacher(fullname=teacher[0]))

    session.add_all(for_teachers)
    session.commit()

    for_classes = []
    for lesson in classes:
        for_classes.append(Discipline(name=lesson[0], teacher_id=lesson[1]))

    session.add_all(for_classes)
    session.commit()

    for_final_table = []
    for ft in final_table:
        for_final_table.append(
            Grade(
                grade=choice(mark),
                date_of=ft[3],
                student_id=ft[1],
                discipline_id=ft[0],
            )
        )

    session.add_all(for_final_table)
    session.commit()


if __name__ == "__main__":
    students, teachers, classes, groups, marks, final_table = prepare_data(
        *generate_data(
            NUMBER_OF_STUDENTS,
            NUMBER_OF_TEACHERS,
            NUMBER_OF_GROUPS,
        )
    )
    insert_data_to_db(students, teachers, classes, groups, marks, final_table)
    print("Well done!")
