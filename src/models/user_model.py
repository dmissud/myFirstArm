class UserModel:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_user(self):
        return {"name": self.name, "age": self.age}