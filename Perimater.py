#21/10/26
#Blake Mans
#task 1 
#Create a program that can caculate area and perimater


#ask for width
#Check that the number is more than zero
error = ("please enter a number more than zero\n")
while True:
    try:
        width =float(input("width:   "))
        if width >0:
            break
        else:
            print(error)
    except ValueError:
        print(error)






     