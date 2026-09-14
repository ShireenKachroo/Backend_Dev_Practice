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

UPDATE Students SET department = 'CSE' WHERE id = 105;
UPDATE Students SET name = 'Anshika Sharma' WHERE name = 'Anshika';

DELETE FROM Students WHERE id = 102;


