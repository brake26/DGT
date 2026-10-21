#21/10/26
#Blake Mans
#task 1 
#Create a program that can caculate area and perimater

def num_check (question):

    #ask for width
    #Check that the number is more than zero
    error = ("please enter a number more than zero\n")
    while True:
        try:
            response =float(input(question))
            if response >0:
                return response
            else:
                print(error)
        except ValueError:
            print(error)

#Main Routine
for item in range (0,2):
    Width = num_check ("width:   ")
    print(Width)

print()

for item in range (0,2):
    Height = num_check ("Height:   ")
    print(Height)


     