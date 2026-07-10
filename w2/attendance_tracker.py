student_list = ["Alice", "Bob", "Charlie", "David", "Eva"]

attendance = {}

def get_attendance_status(student):
    while True:
        att = input(f"Enter p for present or a for absent for {student}: ").strip().lower()
        if att in ("p", "a"):
            return "Present" if att == "p" else "Absent"
        print("Invalid input. Please enter only p or a.")

for i in range(2):
    print(f"\nDay {i + 1} Attendance")
    print("-" * 20)

    attendance[i] = {}
    for student in student_list:
        attendance[i][student] = get_attendance_status(student)

print("\nAttendance Summary")
print("=" * 20)
for day, records in attendance.items():
    print(f"Day {day + 1}:")
    for student, status in records.items():
        print(f"  {student}: {status}")
