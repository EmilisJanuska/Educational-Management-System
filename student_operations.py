from storage import load_data, save_data
from exceptions import InvalidIDException, DuplicateIDException

'''
https://www.youtube.com/watch?v=5ChEesH3KYA
'''

def validate_student(id: str, students: list) -> None:
    if not isinstance(id, str) or not id.strip(): 
        raise InvalidIDException(message='ID must be a non-empty string.', value=101)
        
    for student in students:
        if student["ID"] == id:
            raise DuplicateIDException(message='ID must be a unique non-empty string.', value=102)
            
        
def add_student() -> None:
    students: list = load_data()
    while True:
        print('ENTER STUDENTS DETAILS CAREFULLY.')
        
        student_id: str = input('ID: ')
        try:
            validate_student(student_id, students)
        except(InvalidIDException, DuplicateIDException) as e:
            print(e)
            continue
            
        course: str = input('COURSE: ')
        minor: str = input('MINOR: ')
        
        try:
            year = int(input('YEAR: '))
        except ValueError:
            print('Year must be a number. Try again.')
            continue
        
        confirmation = input('Confrim details are correct (Y/N): ').upper()
        
        if confirmation == 'Y':
            students.append({"ID": id, "Course": course, "Minor": minor, "Year": year})
            save_data(students)
            print('Student added successfully!')
            return
        else:
            print('Details not confirmed.')
        
def view_students() -> None: #prints the raw dict -> try make it UI friendly
    students = load_data()
    if students:
        for student in students:
            print(student)
    else:
        print('Found no students.')
        
        
def update_student() -> None: #ID is  immutable.
    students = load_data()
    student_id = input("Enter Student ID to update: ")
    print('To keep original information leave blank.')                  # !!!!!!!!!!!!!!!NEED TO IMPLEMENT THIS!!!!
    for student in students:
        if student["ID"] == student_id:
            student["Course"] = input('Enter new course: ')
            student["Minor"] = input('Enter new minor: ')
            student['Year'] = input('Enter new year: ')
            save_data(students)
            print("Student updated successfully!")
            return
        
    print('Student not found!')
    
def delete_student():
    students = load_data()
    student_id = input("Enter student ID to delete: ")
    
    students = [student for student in students if student["ID"] != student_id]
    save_data(students)
    print("Student deleted successfully")