class UserController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_user(self):
        user = self.model.get_user()
        self.view.display_user(user)