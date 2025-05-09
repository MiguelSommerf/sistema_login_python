from Views.testeKivy import LoginApp
from NavigationController import NavigationController
from UserController import UserController

class AppController:
    def __init__(self):
        self.userController = UserController()
        self.navigationController = NavigationController()
        
    def View(self):
        if(self.navigationController.getCurrentView == 'LoginApp'):
            loginView = LoginApp()
            loginView.run()

        if(self.navigationController.getCurrentView == 'SignUpApp'):
            # load the view
            pass

