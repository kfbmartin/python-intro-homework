def is_valid_score(score):
    if isinstance(score, int) and score >= 0 and score <=100:
        return True
    else:
        return False

score_input = input("Enter a score: ")

if score_input.isdigit():
    score_input = int(score_input)
    score_result = is_valid_score(score_input)
else:
    score_result = False
    
if score_result == True:

    print("Valid score.")

else:
    print("Invalid score \u2014 must be between 0 and 100.")