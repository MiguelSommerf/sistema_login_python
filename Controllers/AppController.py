from Views.Login import LoginScreen
from Controllers.NavigationController import NavigationController
from Controllers.UserController import UserController

class AppController:
    def __init__(self):
        self.userController = UserController()
        self.navigationController = NavigationController(controller=self)
        
    def View(self, name):
        if name == 'LoginScreen':
            loginView = LoginScreen()
            self.navigationController.add_screen(loginView, 'LoginScreen')

        if name == 'SignUpScreen':
            #signUpView = SignUpApp(controller=self)
            #self.navigationController.add_screen(signUpView, 'SignUp')
            pass

