def Favorite_Animal(name):
    checkList = {'Sophia': 'Cat', 'Victoria': 'Dog', 'Madison': 'Elephant', 'Bill': 'Lion'}
    names = list(checkList.keys())
    if name in names:
        print("Hi ", + str(name) + ", your favorite animal is ", checkList[name])
    else:
        print("ERROR! Name cannot be found in the database! Please do it again!")

