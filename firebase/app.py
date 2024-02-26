import pyrebase
import flask




config = {"#Configurations"}

firebase = pyrebase.initialize_app(config)
database = firebase.database()


# # # database = firebase.database()




def setdata():
    name = "Atharva"
    age = 40
    # data = {'name': name, 'age': age, 'likes_python': True}
    # # database.push(data)
    # # #
    # #
    # #
    userId = name
    # database.child(userId).set(data)


def getdata():
    data = database.child("Atharva").get()

    # print(data.val())
    #
    from collections import OrderedDict
    #
    # Assuming data is an OrderedDict returned by data.val()?
    dataa = data.val()
    # Iterate over the items and print each value
    for key, value in dataa.items():
        print(key)
        print(value)





# setdata()

# getdata()
