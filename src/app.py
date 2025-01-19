from models.user_model import UserModel
from src.views.user_view import UserView
from controllers.user_controller import UserController

if __name__ == "__main__":
    model = UserModel("Daniel", 59)
    view = UserView()
    controller = UserController(model, view)
    controller.show_user()