import pandas as pd
from database import get_connection

students = pd.read_csv("data/students.csv")
marks = pd.read_csv("data/marks.csv")
attendance = pd.read_csv("data/attendance.csv")

students = students.drop_duplicates()
marks = marks.drop_duplicates()
attendance = attendance.drop_duplicates()

connection = get_connection()
cursor = connection.cursor()

print("Connected to MySQL!")

for _, row in students.iterrows():

    query = """
INSERT INTO pipeline_students
(student_id, name, age, department)
VALUES (%s, %s, %s, %s)
ON DUPLICATE KEY UPDATE
name = VALUES(name),
age = VALUES(age),
department = VALUES(department)
"""

    values = (
        int(row["student_id"]),
        row["name"],
        int(row["age"]),
        row["department"]
    )

    cursor.execute(query, values)

connection.commit()

print("Students loaded successfully!")

for _, row in marks.iterrows():

    query = """
    INSERT INTO pipeline_marks
    (student_id, subject, mark)
    VALUES (%s, %s, %s)
    """

    values = (
        int(row["student_id"]),
        row["subject"],
        int(row["mark"])
    )

    cursor.execute(query, values)

connection.commit()

print("Marks loaded successfully!")

for _, row in attendance.iterrows():

    query = """
    INSERT INTO pipeline_attendance
    (student_id, attendance_percentage)
    VALUES (%s, %s)
    """

    values = (
        int(row["student_id"]),
        float(row["attendance_percentage"])
    )

    cursor.execute(query, values)

connection.commit()

print("Attendance loaded successfully!")

cursor.close()
connection.close()

print("ETL completed successfully!")