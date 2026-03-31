# collection_manipulator

`collection_manipulator` is a lightweight, terminal-based Python utility for CRUD management of student records stored in memory.

## Description

This program offers a user-friendly menu to:
- add new student records
- display all students
- update student name and age
- delete student records
- display the set of unique subjects taught

Data is persisted only during runtime (in-memory dictionary). Exiting the program clears all records.

## Features

- Student fields: ID, name, age, grade, subjects
- Subjects input as comma-separated list, stored as list
- Unique ID is used as key in student dictionary
- Console menu with 6 options and validation for invalid choices

## Usage

1. Open a console / terminal in project folder.
2. Run:

```bash
python collection_manipulator.py
```

3. Follow prompts:

- `1` Add Student
- `2` Display All Students
- `3` Update Student Information
- `4` Delete Student
- `5` Display Subjects Offered
- `6` Exit

## Data Model

- `students` (dict):
  - key: `student_id` (int)
  - value: dict with `name`, `age`, `grade`, `subjects`

## Notes

- No file/database persistence.
- Student IDs must be unique.
- Update functionality only changes name and age currently.
- Subjects are shown as a set for unique subject list.

## Future Improvements

- Add persistence via JSON/CSV
- Improve validation (empty entries, non-integer input, duplicates)
- Allow updating grade and subjects
- Add tests and command-line args
