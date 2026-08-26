students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]
#Find the top scorer
top_scorer_name = ""
top_score = 0

for student in students:
    if student["score"] > top_score:
        top_score = student["score"]
        top_scorer_name = student["name"]

print(f"Top scorer: {top_scorer_name} ({top_score})")

#Calculate the class average
total = 0
for student in students:
    total+= student["score"]
average = total / len(students)
print(f"Class average: {average:.1f}")   # Output: Class average: 85.5

#List all unique subjects

subjects = set()
for student in students:
    subjects.add(student["subject"])

print(f"Subjects offered: {subjects}")

#List High Scorers with score over 75
high_scorers = []
for student in students:
    if student["score"] >75:
        high_scorers.append(student["name"])

print(f"High scorers: {high_scorers}")