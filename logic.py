def calculate_attendance(attendance_list):
    if not attendance_list: return 0
    return (sum(attendance_list) / len(attendance_list)) * 100

def get_ai_remark(marks):
    if marks >= 80: return "Good"
    elif marks >= 50: return "Average"
    else: return "Needs Improvement"

def get_attendance_status(percentage):
    return " LOW" if percentage < 75 else " OK"
