#23/10/26
#Blake Mans
#Task 2
#Create a program that can calculate the cost of a fence
#Recycle code from the perimater and area calculator



def num_check (question):
    #ask for the width, Height and cost per meter
    #Check that the number is more than zero

    error = ("please enter a number more than zero\n")
    while True:
        try:
            response = float(input(question))
            if response >0:
                return response
            else:
                print(error)
        except ValueError:
            print(error)

#Main routine
#Actully ask the question
#calculate the numbers
#ask the user if they want too loop
keep_going = ""
while keep_going == "":

    width = num_check ("Width:   ")
    print(width)

    print()

    height = num_check ("Height:  ")
    print(height)

    print()

    cost_per_meter = num_check ("Cost Per Meter:  ")

    perimatar = 2 * (width + height)

    cost = perimatar * cost_per_meter

    print()
    print(f"The perimater of your fence will be {perimatar} units")
    print(f"The cost of your fence will be ${cost}")

    keep_going = ""

    keep_going = input("press enter to keep going or any key to quit:   ")
    print()

print("Thank you for using the fence cost calculator")

