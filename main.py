from fastapi import FastAPI ,HTTPException# type: ignore
from schemas import Student_create,Student_Out
from models import create_student,get_all_students,update_student,delete_student


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


@app.put("/students/{student_id}", response_model=Student_Out)
async def update_student_route(student_id: str, student_data: Student_create):
    updated = await update_student(student_id, student_data.dict())

    if not updated:
        raise HTTPException(status_code= 404 , detail=(f"{student_id} Student Not Found!"))
    
    return updated

@app.delete("/student/{student_id}")
async def delete_student_route(student_id: str):
    deleted = await delete_student(student_id)

    if not deleted:
        raise HTTPException(status_code=404, detail=(f"{student_id} student not Found!"))

    return {"message": f"{student_id} Student deleted successfully!"}
