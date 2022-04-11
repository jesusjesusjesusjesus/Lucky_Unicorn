

def yes_no(question_text):
    while True:
        answer = input(question_text).lower()
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer
        else:
            print("please answer 'yes' or 'no'")

def instructions():
    print("***** instuructions *****")

played_before = yes_no("have you played this game before?: ")

if played_before == "No":
    instructions()
else:
    print("program continues")

