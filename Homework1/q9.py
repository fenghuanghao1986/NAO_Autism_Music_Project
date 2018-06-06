def compare(user1, user2):
    checkList = ['Lion', 'Tiger', 'Zebra']
    if (user1 not in checkList) or (user2 not in checkList):
        print("Invalid input! Try again later!")
    elif user1 == user2:
        print("It's a tie!")
    elif (user1 == "Lion" and user2 == "Tiger") or (user2 == "Lion" and user1 == "Tiger"):
        print("Lion wins!")
    elif (user1 == "Lion" and user2 =="Zebra") or (user2 == "Lion" and user1 =="Zebra"):
        print("Zebra wins!")
    elif (user1 == "Tiger" and user2 =="Zebra") or (user1 == "Tiger" and user2 =="Zebra"):
        print("Tiger wins!")

print("Player1 please enter your choice from : Lion, Tiger and Zebra.")
user1 = raw_input()
print("Player2 please enter your choice from : Lion, Tiger and Zebra.")
user2 = raw_input()

compare(user1, user2)