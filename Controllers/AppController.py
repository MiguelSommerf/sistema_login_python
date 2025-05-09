from Views.testeKivy import LoginApp
from UserController import UserController

class AppController:
    def __init__(self):
        self.userController = UserController()
        self.view
        
    def loginView(self):
        self.view = LoginApp()
        self.view.run()
        
        #UserController methods
        
        
    def SignUpView(self):
        #self.view = SignUpApp()
        
        #UserController methods
        
        return