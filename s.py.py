from pydantic import BaseModel

class Employee(BaseModel):
    name: str
    age: int

employee = Employee(name="Sahil", age=23)

print(employee.name)
print(employee.age)