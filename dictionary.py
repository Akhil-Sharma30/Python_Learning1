#dictionary : it is used for giving a data set a values and its key frame 
def days_to_unit(num_of_days , calculated):
    if calculated == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours
    elif calculated == "minutes":
        return f"{num_of_days} days are {num_of_days * 24} minutes
    else:
        return "enter supported text"

def check():
      try:
    
         user = int(days_and_unit_dictionary["days"])
         if user > 0:
            calculate_value= days_to_unit(user,days_and_unit_dictionary["hours"])
    
      except ValueError:
            print("you didn't entered a valid text please try again")
            
# true is used in while loop if you want it to run till unlimited time
design = ""
while design!= "exit":
    design = input("enter the number of days and unit to be converted with : sign between the input \n ")
    days_and_unit = design.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days":design[0],"hours":design[1]}
    check()