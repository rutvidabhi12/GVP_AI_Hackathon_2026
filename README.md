AI-Assisted Smart Attendance & Performance Tracker
GVP AI Hackathon 2026

Project Overview
This is a modular Python-based application designed to manage student attendance and internal assessment records efficiently. The system replaces manual Excel-based tracking with an automated process that includes AI-driven validation, attendance shortage alerts, and performance analytics.

System Architecture::
The project follows a Modular Design to ensure scalability and clean code management:
main.py: Handles the User Interface (UI), menu navigation, and user inputs.
logic.py: Contains the core AI-assisted logic for calculating percentages, generating warnings, and providing performance remarks.
data_manager.py: Manages data persistence using JSON format, ensuring records are saved permanently.

AI-Assisted Features::
Developed with the assistance of Gemini AI, the system includes:
Auto-generated Sample Data: Automatically populates the system with dummy records for instant testing and demonstration.
Attendance Shortage Warning: A smart logic that flags students with attendance below 75% with a LOW status.
Performance Analytics: Automatically categorizes students based on marks into "Good", "Average", or "Needs Improvement".
Data Validation: Ensures roll numbers are unique and attendance inputs are validated.

How to Run::
Ensure you have Python installed on your system.
Download all three files (main.py, logic.py, data_manager.py) into the same folder.
Run the application using:
Bash
python main.py
Data will be automatically stored in students_data.json.

Expected Output::
Console UI: A clean, tabular report of student standings.
Persistence: Data remains intact even after closing the program.
Insights: Instant identification of students who are at risk due to low attendance.

 
AI Tool Used: Gemini AI
Impact: AI significantly reduced development time by generating complex conditional logic and formatting the tabular output for better readability.
