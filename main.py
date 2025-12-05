from fastapi import FastAPI # type: ignore
from schemas import Student_create,Student_Out
from models import create_student,get_all_students


app = FastAPI(
    title="Student CRUD API with MongoDB",
    description="A fully asynchronous FastAPI CRUD service using Motor and MongoDB.",
    version="1.0.0"
)


@app.post("/students",response_model = Student_Out)
async def add_student(student:Student_create):
    new_student = await create_student(student.dict())
    return new_student

@app.get("/students",response_model =list[Student_Out])
async def fetch_students_():
    students = await get_all_students()
    return students

