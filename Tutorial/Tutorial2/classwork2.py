#Check the input whether a positive integer
valid_input = False
while not valid_input:
    try:
        number = int(input("Enter a positive integer: ")) #input
        if number > 0:
            valid_input = True #The input is positive integer
        else:
            print("Not a positive number. Try again: ") #Occurs when input is negative
    except ValueError:
        print("Not an integer. Try again:") #Occurs when input is not integer
        
#if-loop to check whether the input is the multiple of 2,3,4 
if number%2 ==0 and number%3 ==0 and number%4 == 0:
    print("The number ", number, " is a multiple of 2,3,4")
else:
    print("The number ", number, " is not a multiple of 2,3,4")
print("End of Program") #End of Loop and Stop