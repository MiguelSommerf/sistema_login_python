from kivy.uix.screenmanager import ScreenManager

class NavigationController:
    def __init__(self, controller=None):
        self.screen_manager = ScreenManager()
        self.screen_manager.controller = controller
        
    def add_screen(self, screen, name):
        screen.name = name
        self.screen_manager.add_widget(screen)
        
    def go_to_screen(self, screen_name):
        self.screen_manager.current = screen_name
        
    def get_current_screen(self):
        return self.screen_manager.current_screen.name
    
    def get_screen_manager(self):
        return self.screen_manager