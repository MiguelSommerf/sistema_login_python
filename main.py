from kivymd.app import MDApp
from Controllers.NavigationController import NavigationController

class MainApp(MDApp):
    def build(self):
        self.navigation_controller = NavigationController()
        
        # Calling the method from NavigationController to set the screen
        return self.navigation_controller.get_current_screen()
    
if __name__ == "__main__":
    MainApp().run()