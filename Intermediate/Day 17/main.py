class User:
    def __init__(self,username,user_id):
        self.username = username
        self.id = user_id
        self.followers = 0
        self.following = 0

    def follow(self,user):
        user.followers += 1
        self.following += 1

user_1 = User("rynlkl","001")
user_2 = User("kayliyeoql","002")

user_1.follow(user_2)
print(user_1.following)
print(user_2.followers)



#constructor initialises the class' starting functions
## def __init__(self)
