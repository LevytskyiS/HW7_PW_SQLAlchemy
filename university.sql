-- Table: groups
DROP TABLE IF EXISTS groups;
CREATE TABLE groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_name VARCHAR(50) UNIQUE NOT NULL
);

-- Table: students
DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student VARCHAR(255) UNIQUE NOT NULL,
    group_id VARCHAR(50),
    FOREIGN KEY (group_id) REFERENCES groups (id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- Table: teachers
DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    teacher VARCHAR(255) UNIQUE NOT NULL
);

-- Table: classes
DROP TABLE IF EXISTS classes;
CREATE TABLE classes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lesson VARCHAR(255) UNIQUE NOT NULL,
    teacher_id VARCHAR(255),
    FOREIGN KEY (teacher_id) REFERENCES teachers (id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- Table: marks
DROP TABLE IF EXISTS marks;
CREATE TABLE marks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lesson_id INTEGER NOT NULL,
    student_id INTEGER NOT NULL,
    mark INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (lesson_id) REFERENCES classes (id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
    FOREIGN KEY (student_id) REFERENCES students (id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);