

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


show_intructions = yes_no("have you played this game before?: ")
print(f"You entered '{show_intructions}'")
print()
having_fun = yes_no("are you having fun?: ")
print(f"You entered '{having_fun}'")
