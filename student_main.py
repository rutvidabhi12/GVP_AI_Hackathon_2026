import data_manager as dm
import logic

def show_report(students):
    print("\n" + "="*70)
    print(f"{'Roll':<5} {'Name':<12} {'Attnd%':<10} {'Status':<12} {'Remark':<15}")
    print("="*70)
    for s in students:
        pct = logic.calculate_attendance(s['Attnd'])
        status = logic.get_attendance_status(pct)
        remark = logic.get_ai_remark(s['Marks'])
        print(f"{s['Roll']:<5} {s['Name']:<12} {pct:<10.1f} {status:<12} {remark:<15}")

def mark_attendance(students):
    print("\n--- Mark Daily Attendance (y for Present / n for Absent) ---")
    for s in students:
        val = input(f"Is {s['Name']} (Roll: {s['Roll']}) Present? (y/n): ").lower()
        # AI-Assisted Validation: Convert y/n to 1/0
        s['Attnd'].append(1 if val == 'y' else 0)
    dm.save_data(students)
    print("Attendance saved successfully!")

def main():
    students = dm.load_data()
    if not students:
        students = dm.get_sample_data()
        dm.save_data(students)

    while True:
        print("\n--- Smart Tracker Menu ---")
        print("1. View Student Report")
        print("2. Mark Attendance (Daily)")
        print("3. Add New Student")
        print("4. Exit")
        choice = input("Select Option: ")

        if choice == '1':
            show_report(students)
        elif choice == '2':
            mark_attendance(students)
        elif choice == '3':
            roll = input("Enter Roll No: ")
            name = input("Enter Name: ")
            marks = float(input("Enter Marks: "))
            students.append({"Roll": roll, "Name": name, "Sem": "3", "Attnd": [], "Marks": marks})
            dm.save_data(students)
        elif choice == '4':
            break

if __name__ == "__main__":
    main()
