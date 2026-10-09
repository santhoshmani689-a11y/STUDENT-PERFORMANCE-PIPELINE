import pandas as pd
from database import get_connection

# Connect to MySQL
connection = get_connection()

# Read final report
query = """
SELECT *
FROM final_student_report
"""

report = pd.read_sql(query, connection)

print("FINAL STUDENT REPORT")
print(report)

print("\nTOP STUDENTS")

top_students = report.sort_values(
    by="average_mark",
    ascending=False
)

print(top_students[
    ["name", "department", "average_mark"]
].head(5))

print("\nDEPARTMENT PERFORMANCE")

department_report = (
    report.groupby("department")["average_mark"]
    .mean()
    .sort_values(ascending=False)
)

print(department_report)

print("\nAT-RISK STUDENTS")

at_risk = report[
    report["risk_status"] == "At Risk"
]

print(at_risk)
print("Connected to MySQL successfully!")
connection.close()