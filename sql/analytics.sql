SELECT
    s.student_id,
    s.name,
    s.department,
    m.subject,
    m.mark
FROM pipeline_students s
JOIN pipeline_marks m
ON s.student_id = m.student_id;

SELECT
    s.student_id,
    s.name,
    s.department,
    SUM(m.mark) AS total_marks
FROM pipeline_students s
JOIN pipeline_marks m
ON s.student_id = m.student_id
GROUP BY
    s.student_id,
    s.name,
    s.department;

SELECT
    s.student_id,
    s.name,
    s.department,
    AVG(m.mark) AS average_mark
FROM pipeline_students s
JOIN pipeline_marks m
ON s.student_id = m.student_id
GROUP BY
    s.student_id,
    s.name,
    s.department;

SELECT
    s.name,
    s.department,
    SUM(m.mark) AS total_marks
FROM pipeline_students s
JOIN pipeline_marks m
ON s.student_id = m.student_id
GROUP BY
    s.student_id,
    s.name,
    s.department
ORDER BY total_marks DESC;

SELECT
    s.department,
    AVG(m.mark) AS average_mark
FROM pipeline_students s
JOIN pipeline_marks m
ON s.student_id = m.student_id
GROUP BY s.department
ORDER BY average_mark DESC;

SELECT
    s.name,
    s.department,
    AVG(m.mark) AS average_mark,
    a.attendance_percentage
FROM pipeline_students s
JOIN pipeline_marks m
ON s.student_id = m.student_id
JOIN pipeline_attendance a
ON s.student_id = a.student_id
GROUP BY
    s.student_id,
    s.name,
    s.department,
    a.attendance_percentage;

SELECT
    s.name,
    s.department,
    AVG(m.mark) AS average_mark,
    a.attendance_percentage
FROM pipeline_students s
JOIN pipeline_marks m
ON s.student_id = m.student_id
JOIN pipeline_attendance a
ON s.student_id = a.student_id
GROUP BY
    s.student_id,
    s.name,
    s.department,
    a.attendance_percentage
HAVING
    AVG(m.mark) < 50
    OR a.attendance_percentage < 75;