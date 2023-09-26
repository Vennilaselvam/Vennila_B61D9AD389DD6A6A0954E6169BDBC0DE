def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Define a Student class
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

# Example usage
if __name__ == "__main__":
    # Create a list of student objects
    students = [
        Student("Alice", "S001", 3.8),
        Student("Bob", "S002", 3.5),
        Student("Charlie", "S003", 4.0),
        Student("David", "S004", 3.9)
    ]

    # Sort the students by CGPA
    sorted_students = sort_students(students)

    # Print the sorted list of students
    for student in sorted_students:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")