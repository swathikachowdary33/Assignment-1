student = {
    "name": "John",
    "age": 21,
    "marks": {"math": 80, "science": 90}
}

# Accessing name using get()

name = student.get("name")
print(name)

#Adding a  new key grade using assignment

student["grade"] = "A"
print(student)

#Update age using update()

student.update({"age": 25})     
print(student)

#Remove age using pop

student.pop("age")
print(student)

# Remove last inserted item using popitem()

last_item=student.popitem()
print(student)

#Get all keys using keys()

keys = student.keys()
print(keys)

#Get all values using values()

values=student.values()
print(values)

#Get all items using items()

items=student.items()
print(items)

#Use setdefault() to add city

student.setdefault("city","Hyderbad")
print(student)

#Merge another dictionary using update()

other={"city": "Hyderbad","grade":"A"}
student.update(other)
print(student)