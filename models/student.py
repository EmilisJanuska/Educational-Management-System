from exceptions import InvalidIDException


class Student():
    def __init__(self, id, course, year):
        self.__id = id
        self.__course = course
        self.__year = year
        
    @property
    def student_id(self) -> str:
        return self.__id
       
    @student_id.setter
    def student_id(self, new_id: str) -> None:
        if not isinstance(new_id, str) or not new_id.strip():
            raise InvalidIDException(message='ID must be a non-empty string', value=101)
              
        self.__id = new_id
       
    @property
    def student_course(self):
        return self.__course
        
    @student_course.setter
    def student_course(self, new_course: str) -> None:
        if not isinstance(new_course, str) or not new_course.strip():
            raise ValueError('Course should be a non-empty string!')
            
        self.__course = new_course
        
    @property
    def student_year(self) -> int:
        return self.__year
        
    @student_year.setter
    def student_year(self, new_year: int) -> None:
        if not isinstance(new_year, int) or new_year <= 0:
            raise ValueError('Year should be a positive integer above zero.')
            
        self.__year = new_year
        
    def get_student_details(self):
        return (f'ID: "{self.__id}"\nCOURSE: "{self.__course}"\nYEAR: "{self.__year}"')