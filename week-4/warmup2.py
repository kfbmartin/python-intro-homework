#Warmup 2 Dictonary Operations

students = {
    "name": "Khalilah",
    "grade": "A",
    "subjects": ["English", "Math", "Computer Science"]
}
for key, value in students.items():
    print(f"{key}: {value}")

students["graduated"] = False

for key, value in students.items():
    print(f"{key}: {value}")
