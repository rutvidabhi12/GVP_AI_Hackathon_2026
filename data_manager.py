import json
import os

FILE_NAME = "students_data.json"

def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as f:
            return json.load(f)
    return []

def save_data(data):
    with open(FILE_NAME, 'w') as f:
        json.dump(data, f, indent=4)

def get_sample_data():
    return [
        {"Roll": "101", "Name": "Amit", "Sem": "3", "Attnd": [1, 1, 0, 1], "Marks": 82},
        {"Roll": "102", "Name": "Priya", "Sem": "3", "Attnd": [0, 0, 1, 0], "Marks": 45},
        {"Roll": "103", "Name": "Raj", "Sem": "3", "Attnd": [1, 1, 1, 1], "Marks": 65}
    ]
