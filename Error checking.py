#Error Checking
#Blake Mans
#25/09/26
#V1

done = True
 # Boolean varible set to True
'''while done:
    num = int(input("Please enter your value as an interger: "))
    done = False
    print(f"the number you enterd is {num}")'''
#use try and except to catch errors
'''done = False
while not done:
    try:
        num = float(input("Please enter a number:"))
        done = True

    except ValueError:
        print("That is not a valid float number. \n")

print(f"The number you entered is {num}")'''

#recycling code with a function
#create a function to call every time I ask the user
#for a bumber a function is a chunk of code that does something

def input_check():
    while True:
        try:
            num = float(input("Please enter a number:"))
            break
        except ValueError:
            print("That is not a valid float number. \n")

    print(f"the number you entered is {num}")

#main routine
input_check()