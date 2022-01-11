#while loop 
def check(userdata):
      try:
    
         user = int(userdata)
         if user > 0:
            print("your text is fine ")
    
      except ValueError:
            print("you didn't entered a valid text please try again")
            
# true is used in while loop if you want it to run till unlimited time
design = ""
while design!= "exit":
    design = input()
    check(design)