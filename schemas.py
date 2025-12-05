from pydantic import BaseModel # type: ignore


class Student(BaseModel):
    name:str
    father_name:str
    student_class:str
    age:int
    fees:float

class Student_create(Student):
    pass

class Student_Out(Student):
    id:str

