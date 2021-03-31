#This file takes the input from the user

def getInput():
    while True:
        try: 
            text = input("Enter the user id and the top K value: ")
            userId, topK = text.split(' ')
            return int(userId), int(topK)
        except:
            print("Invalid input. Try again")