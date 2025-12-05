from bson import ObjectId # type: ignore
from db import db


def student_helper(student)-> dict:
    return {
        "id" : str(student["_id"]),
        "name": str(student["name"]),
        "father_name":str(student["father_name"]),
        "student_class":str(student["student_class"])
        ,"age":int(student["age"]),
        "fees":float(student["fees"])
}

collection = db.students

# create_student

async def create_student(data:dict):
    result = await collection.insert_one(data)
    new_student=await collection.find_one({"_id":result.inserted_id})
    return student_helper(new_student)



# get_all_students

async def get_all_students():
    students= []
    async for student in collection.find():
        students.append(student_helper(student))

    return students


# update_student

async def update_student(student_id:str,data:dict):
    updated = await collection.update_one(
        {
            "_id":ObjectId(student_id),
            "$set":data
        }
    )
    if updated.modified_count ==0:
        return None
    new_data = await collection.find_one({"_id":ObjectId(student_id)})
    return student_helper(new_data)

async def delete_student(student_id:str):
    deleted = await collection.delete_one({"_id":ObjectId(student_id)})
    return deleted.deleted_count > 0