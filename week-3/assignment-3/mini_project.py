day = input("What day is it? ").lower()

if day=="Sunday":
    timeOfDay = input("What time of day? ").lower()
    if(timeOfDay == "morning"):
        print("Suggestion: Good Morning, it's a great time to go for a walk!")
    elif(timeOfDay == "afternoon"):
        print("Suggestion: It's time for lunch.")
    elif(timeOfDay == "evening"):
        print("Suggestion: Good evening, it's time to make dinner!")
    else:
        print(f"Sorry, I don't recognize that time of day. Try: morning, afternoon or evening for the time of day on {day}.")

elif day=="Monday":
    timeOfDay = input("What time of day? ").lower()

    if(timeOfDay =='morning'):
        print("Suggestion: Morning, it's a great time to make Pancakes for Breakfast!")
    elif(timeOfDay == "afternoon"):
        print("Suggestion: Good afternoon, it's a great time to read a book!")
    elif(timeOfDay == "evening"):
        print("Suggestion: Good evening, it's a great time to go to a friend's house.")
    else:
        print(f"Sorry, I don't recognize that time of day. Try: morning, afternoon or evening for the time of day on {day}.")
        
elif day=="Tuesday":
    timeOfDay = input("What time of day? ").lower()

    if(timeOfDay =='morning'):
        print("Suggestion: Morning, it's a great time to go to a Cafe for Breakfast!")
    elif(timeOfDay == "afternoon"):
        print("Suggestion: Good afternoon, it's a great time to go to lunch!")
    elif(timeOfDay == "evening"):
        print("Suggestion: Good evening, it's a great time to go to the gym!")
    else:
        print(f"Sorry, I don't recognize that time of day. Try: morning, afternoon or evening for the time of day on {day}.")

elif day=="Wednesday":
    timeOfDay = input("What time of day? ").lower()

    if(timeOfDay =='morning'):
        print("Suggestion: Morning, it's a great time to go for a run!")
    elif(timeOfDay == "afternoon"):
        print("Suggestion: Good afternoon, it's a great time to go to the grocery store.")
    elif(timeOfDay == "evening"):
        print("Suggestion: Good evening, it's a great time to a restaurant!")
    else:
        print(f"Sorry, I don't recognize that time of day. Try: morning, afternoon or evening for the time of day on {day}.")

elif day=="Thursday":
    timeOfDay = input("What time of day? ").lower()

    if(timeOfDay =='morning'):
        print("Suggestion: Morning, it's a great time to have coffee!")
    elif(timeOfDay == "afternoon"):
        print("Suggestion: Good afternoon, it's a great time to go to the post office.")
    elif(timeOfDay == "evening"):
        print("Suggestion: Good evening, it's a great time to walk the dog!!")
    else:
        print(f"Sorry, I don't recognize that time of day. Try: morning, afternoon or evening for the time of day on {day}.")

elif day=="Friday":
    timeOfDay = input("What time of day? ").lower()

    if(timeOfDay =='morning'):
        print("Suggestion: Morning, it's a great time to exercise!")
    elif(timeOfDay == "afternoon"):
        print("Suggestion: Good afternoon, it's a great time to play Ping Pong.")
    elif(timeOfDay == "evening"):
        print("Suggestion: Good evening, it's a great time to watch TV!")
    else:
        print(f"Sorry, I don't recognize that time of day. Try: morning, afternoon or evening for the time of day on {day}.")

elif day=="Saturday":
    timeOfDay = input("What time of day? ").lower()

    if(timeOfDay =='morning'):
        print("Suggestion: Morning, it's a great time watch the news!")
    elif(timeOfDay == "afternoon"):
        print("Suggestion: Good afternoon, it's a great time to go for Ice Cream!")
    elif(timeOfDay == "evening"):
        print("Suggestion: Good evening, it's a great time to watch a movie!")
    else:
        print(f"Sorry, I don't recognize that time of day. Try: morning, afternoon or evening for the time of day on {day}.")
else:
    print("Sorry, I don't recognize that day. Try: Monday, Tuesday, Wednesday...")

