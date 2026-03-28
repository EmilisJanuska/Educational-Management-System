import student_operations
import sys
import os

def main() -> None:
    while True:
        print('\n-----Main Menu-----')
        print('1. View Students')
        print('2. Add Student')
        print('3. Update Student')
        print('4. Delete Student')
        print('5. Exit')
        print('-------------------')
        try:
            user_choice: int = int(input('>>>'))
            
            if user_choice == 5:
                print('Exiting program...')
                sys.exit()

            elif user_choice == 1:
                student_operations.view_students()
                input('Press enter to continue.')
                
            elif user_choice == 2:
                student_operations.add_student()
                input('\nPress enter to continue.')
                
            elif user_choice == 3:
                student_operations.update_student()
                input('\nPress enter to continue.')
                
            elif user_choice == 4:
                student_operations.delete_student()
                input('\nPress enter to continue.')
                
            else:
                print(f'\nTry again. {user_choice} is not an option ...')
                
                            
        except TypeError:
            print('Select options from 1-5 only ...')
            
        
            
    
if __name__ == "__main__":
    main()