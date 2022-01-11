#error handling and try catch loop 

def check(userdata):
      try:
    
         user = int(userdata)
         if user > 0:
            print("your text is fine ")
    
      except ValueError:
            print("you didn't entered a valid text please try again")
            
design = input()
check(design)