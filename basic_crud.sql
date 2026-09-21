DROP TABLE Students;

CREATE TABLE Students(
	id INT PRIMARY KEY,
	name TEXT,
	department TEXT
);

INSERT INTO Students (id, name, department)
VALUES (101, 'Shireen', 'CSE'), 
(102,'Anshika','CSE'),
(103, 'Khushi', 'AI/ML'), 
(105, 'Dhruvi','DS');

SELECT * FROM Students;
SELECT name, department FROM Students;
SELECT * FROM Students WHERE department = 'CSE';

UPDATE Students SET dept = 'CSE' WHERE id = 103;
DELETE FROM Students WHERE id = 103;

SELECT * FROM Students WHERE id > 101;
SELECT name, department FROM Students WHERE department = 'CSE';
SELECT * FROM Students WHERE id <> 102;

SELECT * FROM Students WHERE department = 'CSE' AND id > 101;
SELECT * FROM Students WHERE department = 'CSE' OR department = 'AI/ML';
SELECT * FROM Students WHERE department <> 'CSE';
SELECT *  FROM Students WHERE department = 'CSE' AND (id = 101 OR id = 102);

SELECT * FROM Students WHERE department IN ('CSE','AI/ML');
SELECT * FROM Students WHERE id BETWEEN 101 AND 103;
SELECT * FROM Students WHERE id NOT BETWEEN 101 AND 103;

SELECT * FROM Students WHERE name LIKE 'S%';
SELECT * FROM Students WHERE name LIKE '%hi%';
SELECT * FROM Students WHERE name LIKE '%i';
SELECT * FROM Students WHERE name ILIKE 's%';

SELECT * FROM Students ORDER BY id DESC;
SELECT * FROM Students ORDER BY name;
SELECT * FROM Students ORDER BY department, name DESC;

SELECT * FROM Students ORDER BY id ASC LIMIT 2;
SELECT * FROM Students ORDER BY id ASC LIMIT 2 OFFSET 2;
SELECT * FROM Students LIMIT 5 OFFSET 10;

SELECT COUNT(*) FROM Students;
SELECT MIN(id) FROM Students;
SELECT MAX(id) FROM Students;
SELECT AVG(id) FROM Students;
SELECT COUNT(*) AS total_students FROM Students;

SELECT department, COUNT(*) FROM Students GROUP BY department;
SELECT department, AVG(id) FROM Students GROUP BY department;
SELECT department, COUNT(*) AS student_count FROM Students GROUP BY department;

SELECT department, COUNT(*) FROM Students GROUP BY department HAVING COUNT(*) >= 2;
SELECT department, COUNT(*) FROM Students GROUP BY department HAVING COUNT(*) = 1 ;
SELECT department, AVG(id) FROM Students GROUP BY department HAVING AVG(id) > 102;
SELECT department, COUNT(*) FROM Students WHERE id > 101 GROUP BY department HAVING COUNT(*) > 1;

CREATE TABLE Departments(
    id INT PRIMARY KEY,
    name TEXT
);

INSERT INTO Departments (id, name)
VALUES
(1, 'CSE'),
(2, 'AI/ML'),
(3, 'DS');

SELECT * FROM Departments;

SELECT s.name, d.name FROM Students s INNER JOIN Departments d ON s.department = d.name;
SELECT s.name, d.name FROM Students s LEFT JOIN Departments d ON s.department = d.name;
SELECT s.name, d.name FROM Students s RIGHT JOIN Departments d ON s.department = d.name;

SELECT s.name, d.name FROM Students s INNER JOIN Departments d ON s.department = d.name WHERE s.department = 'CSE';
SELECT s.name, d.name FROM Students s LEFT JOIN Departments d ON s.department = 'AI/ML' WHERE d.name = 'AI/ML';

ALTER TABLE Students
ADD COLUMN department_id INT;

UPDATE Students
SET department_id = 1
WHERE department = 'CSE';

UPDATE Students
SET department_id = 2
WHERE department = 'AI/ML';

UPDATE Students
SET department_id = 3
WHERE department = 'DS';

SELECT * FROM Students;

ALTER TABLE Students
ADD CONSTRAINT fk_students_department
FOREIGN KEY (department_id)
REFERENCES Departments(id);

SELECT s.name AS student_name, d.name AS department_name
FROM Students s
JOIN Departments d
ON s.department_id = d.id;

ALTER TABLE Students
DROP COLUMN department;

CREATE INDEX idx_students_department ON Students(department_id);
