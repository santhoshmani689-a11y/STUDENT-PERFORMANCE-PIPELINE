import pandas as pd
import matplotlib.pyplot as plt

from database import get_connection


connection = get_connection()

query = """
SELECT *
FROM final_student_report
"""

report = pd.read_sql(query, connection)

connection.close()



department_report = (
    report.groupby("department")["average_mark"]
    .mean()
    .sort_values(ascending=False)
)

department_report.plot(kind="bar")

plt.title("Average Marks by Department")
plt.xlabel("Department")
plt.ylabel("Average Mark")
plt.tight_layout()
plt.savefig("department_performance.png", dpi=300)
plt.show()
plt.close()

top_students = report.nlargest(5, "average_mark").sort_values(
    "average_mark"
)

plt.figure()
plt.barh(top_students["name"], top_students["average_mark"])
plt.title("Top 5 Students by Average Marks")
plt.xlabel("Average Mark")
plt.ylabel("Student")
plt.tight_layout()
plt.savefig("top_students.png", dpi=300)
plt.show()
plt.close()



plt.figure()
plt.scatter(
    report["attendance_percentage"],
    report["average_mark"]
)
plt.title("Attendance vs Average Marks")
plt.xlabel("Attendance (%)")
plt.ylabel("Average Mark")
plt.tight_layout()
plt.savefig("attendance_vs_marks.png", dpi=300)
plt.show()
plt.close()

print("All three charts saved successfully!")
