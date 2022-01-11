#list and for loop 

#creating list for general case 
us = ["jan", "feb","mar"]
print(us[0])
us.append("april")
print(us[3])

def check(userdata):
      try:
    
         user = int(num_of_days_elements)
         if user > 0:
            print("your text is fine ")
    
      except ValueError:
            print("you didn't entered a valid text please try again")
            
# true is used in while loop if you want it to run till unlimited time
design = ""
while design!= "exit":
    design = input()
    # in this for loop we are inputting the number in the form of list using split() command to conert string data type to list 
    for num_of_days_elements in design.split(","):
        #output should be the format 20,30,etc "," is used to separate the list elements as we mention split(",") 
        check(design)