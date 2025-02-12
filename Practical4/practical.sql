create database University;
show databases;
USE University;
--Завдання 1
CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(100),
    birth_date DATE
);

CREATE TABLE Courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100),
    credits INT
);

CREATE TABLE Enrollments (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);


--Завдання 2
ALTER TABLE Students ADD COLUMN phone_number VARCHAR(15);

ALTER TABLE Students
DROP COLUMN phone_number;

CREATE TABLE Departments (
	department_id INT PRIMARY KEY,
	department_name VARCHAR(100),
	faculty VARCHAR(100)
);

--Завдання 3
INSERT INTO Students (student_id, first_name, last_name,  email, birth_date) VALUES
(1, 'Іван', 'Іванов', 'ivan.ivanov@example.com', '2000-05-15'),
(2, 'Марія', 'Петренко', 'maria.p@example.com', '1998-11-20'),
(3, 'Олексій', 'Сидоренко', 'oleksiy.sidorenko@example.com', '2001-02-10'),
(4, 'Андрій', 'Коваленко', 'andriy.kovalenko@example.com', '1999-08-30'),
(5, 'Олена',  'Шевченко', 'olena.shevchenko@example.com', '2000-12-05');

INSERT INTO Courses (course_id, course_name, credits) VALUES
(101, 'Математика', 5),
(102, 'Інформатика', 4),
(103, 'Фізика', 3),
(104, 'Хімія', 4),
(105, 'Біологія', 3);

UPDATE Students
SET email = 'john.doe2025@gmail.com'
WHERE student_id = 1;

DELETE FROM Students
WHERE student_id = 3;

--Завдання 4

SELECT * FROM Students;

SELECT * FROM Students
WHERE birth_date > '2000-01-01';

SELECT * FROM Courses
ORDER BY credits ASC;

SELECT COUNT(*) AS count_student FROM Students;

SELECT COUNT(*) AS enrollment_count
FROM enrollments;

INSERT INTO Enrollments (enrollment_id, student_id, course_id, enrollment_date) VALUES
(1, 1, 101, '2025-02-12'),
(2, 2, 102, '2025-02-12');

--Завдання 5

SELECT s.last_name AS student_name, c.course_name
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
JOIN Courses c ON e.course_id = c.course_id;

SELECT s.last_name AS student_name
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
WHERE e.course_id = 102;

SELECT s.last_name AS student_name
FROM Students s
LEFT JOIN Enrollments e ON s.student_id = e.student_id
WHERE e.student_id IS NULL;

ALTER TABLE Enrollments
ADD COLUMN grade VARCHAR(5);

UPDATE Enrollments
SET grade = 'A'
WHERE enrollment_id = 1;

UPDATE Enrollments
SET grade = 'B'
WHERE enrollment_id = 2;

SELECT s.last_name AS student_name
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
JOIN Courses c ON e.course_id = c.course_id
WHERE c.course_id = (
    SELECT course_id
    FROM Courses
    ORDER BY credits DESC
    LIMIT 1
);
