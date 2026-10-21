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
keep_going =""
while keep_going =="":

    Width = num_check ("width:   ")
    print(Width)

    print()

    Height = num_check ("Height:   ")
    print(Height)


    area = Width * Height

    perimator= 2 * (Width + Height)

    print()
    print(f"Perimator: {perimator} units")
    print(f"area: {area} square units")

    keep_going = ""


    keep_going = input("press enter to keep going or any key to quit")
    print()

print("thank you for using the area/perimator calculator")