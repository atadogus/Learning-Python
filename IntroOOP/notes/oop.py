class User:  # when creating a class, some sort of code must be indented in it in order for it not to throw out an error
    # pass  # this keyword allows us to create empty classes or methods without resulting with the aforementioned error
    def __init__(self, user_id, username):  # this is the method used for creating a constructor of the class
        # self.id = id
        self.id = user_id
        self.username = username  # seems like unlike other programming languages I use, I do not have to initialize the variables before the constructor
        # to call or use the variables defined in the constructor, the key defined by self. is used. It does not have to share the same name with the parameter which it
        self.followers = 0  # variables can be initialized within the constructor itself besides being defined by a parameter
        # corresponds to but by convention, it is better to give the same name in the self. declaration as well
        self.following = 0

    def follow(self, user):  # a method defined in a class must automatically have "self" as a parameter unlike methods defined outside a class
        user.followers += 1
        self.following += 1


user_1 = User("001", "ata")
user_2 = User("002", "edaaaaaaa")

print(user_1.following)
user_1.follow(user_2)

# print(user_1.id)
print(user_1.following)