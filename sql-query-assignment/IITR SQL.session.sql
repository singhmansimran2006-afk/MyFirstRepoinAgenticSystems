CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    score INT,
    passed BOOLEAN,
    class INT
);

INSERT INTO students (id, name, score, passed, class)
VALUES  (1, 'Aarav' ,92 , TRUE, 10),
        (2, 'Diya', 76, TRUE, 10),
        (3, 'Rohan', 65, FALSE, 9),
        (4, 'Meera', 88, TRUE, 10),
        (5, 'Kabir', 54, FALSE, 9),
        (6, 'Ananya', 95, TRUE, 10),
        (7, 'Rahul', 81, TRUE, 9),
        (8, 'Sneha', 83, TRUE, 9),
        (9, 'Arjun', 84, TRUE, 10),
        (10, 'Kavya', 69, FALSE, 9);


SELECT * FROM students;

SELECT name,score From students;

SELECT * FROM students
WHERE score > 80;

SELECT * FROM students
WHERE score > 80 AND passed = TRUE;

SELECT * FROM students
WHERE score > 85 OR class = 9;

SELECT * FROM students
WHERE NOT passed = TRUE;

SELECT DISTINCT class FROM students;

SELECT * FROM students
ORDER BY score DESC
LIMIT 5; 

SELECT * FROM students
ORDER BY class ASC, score DESC;

SELECT score AS final_score FROM students;

SELECT name,score FROM students
WHERE score > 75
ORDER BY score DESC
LIMIT 3;