score = int(input("Pick any number between 0 and 100: "))

if score >= 90 and score <=100:
    print(f"Score: {score}")
    print("Grade: A")
elif score >= 80 and score <=89:
    print(f"Score: {score}")
    print("Grade: B")
elif score >= 70 and score <=79:
    print(f"Score: {score}")
    print("Grade: C")
elif score >= 60 and score <=69:
    print(f"Score: {score}")
    print("Grade: D")
elif score >= 0 and score <=59:
    print(f"Score: {score}")
    print("Grade: F")
