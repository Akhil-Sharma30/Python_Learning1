#validating user input

calculation = 20*30*60

def dys(days_entered):
    
    # boolean value check for true or false 
    print(days_entered >= 0)
    #checking its type 
    print(type(days_entered > 0))
    
    if days_entered > 0:
        return (f"the parameters output are {days_entered * calculation} seconds")
    elif days_entered == 0:
        return ("you entered 0 value enter valid number ")
    else :
        return ("please enter the valid number ")

answer = input("hey user enter the number of days \n")
user_data = int(answer)
user_input = dys(user_data)
print(user_input)