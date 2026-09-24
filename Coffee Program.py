#Creating a coffee That a user will be able to interact with
#Blake Mans
#23/09/26
#V1

#TODO: record an input (Store the answer) 
#Check for valid answer
#Ask questions and respond

#Ask the user whether they like coffee or not
like_coffee = input("Do you like coffee? ")
print(like_coffee)
print(f"Your answer was {like_coffee}")

if like_coffee == "yes" or like_coffee == "Yes" or like_coffee == "y":print("good job")
else:print("why")

#V2
# While loop to test the program

keep_going = ""
while keep_going == "":
    like_coffee = input("Do you like coffee? ")
    print(like_coffee)
    print(f"Your answer was {like_coffee}")
    if like_coffee == "yes" or like_coffee == "Yes" or like_coffee == "Y":print("good job")
    keep_going = "Finish"
    if like_coffee == "no" or like_coffee == "No" or like_coffee == "N":print("Why")
    else:print("What")