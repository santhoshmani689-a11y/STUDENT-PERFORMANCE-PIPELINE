import pandas as pd

students = pd.read_csv("data/students.csv")
marks = pd.read_csv("data/marks.csv")
attendance = pd.read_csv("data/attendance.csv")

students = students.drop_duplicates()
marks = marks.drop_duplicates()
attendance = attendance.drop_duplicates()

print("Students missing values:")
print(students.isnull().sum())

print("\nMarks missing values:")
print(marks.isnull().sum())

print("\nAttendance missing values:")
print(attendance.isnull().sum())

print("\nStudent duplicates:")
print(students.duplicated().sum())

print("\nMarks duplicates:")
print(marks.duplicated().sum())

print("\nAttendance duplicates:")
print(attendance.duplicated().sum())

print("\nStudents data types:")
print(students.dtypes)

print("\nMarks data types:")
print(marks.dtypes)

print("\nAttendance data types:")
print(attendance.dtypes)

invalid_marks = marks[
    (marks["mark"] < 0) |
    (marks["mark"] > 100)
]

print("\nInvalid marks:")
print(invalid_marks)

invalid_attendance = attendance[
    (attendance["attendance_percentage"] < 0) |
    (attendance["attendance_percentage"] > 100)
]

print("\nInvalid attendance:")
print(invalid_attendance)

invalid_age = students[
    (students["age"] < 15) |
    (students["age"] > 30)
]

print("\nInvalid student ages:")
print(invalid_age)

invalid_mark_students = marks[
    ~marks["student_id"].isin(students["student_id"])
]

print("\nMarks with invalid student IDs:")
print(invalid_mark_students)

invalid_attendance_students = attendance[
    ~attendance["student_id"].isin(students["student_id"])
]

print("\nAttendance with invalid student IDs:")
print(invalid_attendance_students)

clean_students = students.copy()
clean_marks = marks.copy()
clean_attendance = attendance.copy()