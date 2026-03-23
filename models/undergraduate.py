from models.student import Student


class undergraduate(Student):
    
    def __init__(self, id, course, year, minor):
        super().__init__(id, course, year)
        self.__minor = minor
        
    @property
    def student_minor(self) -> str:
        return self.__minor
        
    student_minor.setter
    def minor(self, new_minor: str):
        if not isinstance(new_minor, str) or not new_minor.strip():
            raise ValueError("Minor must be a non-empty string!")
            
        self.__minor = new_minor
    
    def get_details(self):
        details = super().get_student_details()
        print(f'{details}\nMINOR: "{self.__minor}"')
    
        

