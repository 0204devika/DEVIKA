import random
actual_number=random.randint(1, 100)            #to generate a random number between 1 and 100
while True:
    guess=input("Guess the number between 1 and 100: ")
    if guess.isdigit():
        if int(guess)<1 or int(guess)>100:         #check if number is guessed out of range
            print("Please enter the number between 1 and 100.")
        elif int(guess)<actual_number:
            print("too low")
        elif int(guess)==actual_number:
            print("you guessed it")
            break
        else:
            print("too high")
    else:                                          
       print("enter valid input")       #if input is not a valid digit
                
            
            