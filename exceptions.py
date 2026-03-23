from typing import Any


class InvalidIDException(Exception):
    def __init__(self, message: str, value: Any) -> None:
        super().__init__(message)
        self.message = message
        self.value = value
    
    def __str__(self) -> str:
        return f'{self.message} (Value: {self.value})'

        
class DuplicateIDException(Exception):
    def __init__(self, message: str, value: Any) -> None:
        super().__init__(message)
        self.message = message
        self.value = value
        
    def __str__(self) -> str:
        return f'{self.message} (Value: {self.value})'