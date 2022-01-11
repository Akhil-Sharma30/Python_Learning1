#user input 
answer = input("hey user enter the number of days \n")

#cascading the variable string into int 
int(answer)

calculation = 20*30*60
print("entered number" + answer)
    
print("\n")

#part 2 
      
def dys(days_entered):
    return (f"the parameters output are {days_entered * calculation} seconds")

user_input = dys(20)
print(user_input)