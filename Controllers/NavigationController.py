from kivy.uix.screenmanager import ScreenManager

class NavigationController:
    def __init__(self):
        self.screenManager = ScreenManager()

    def setCurrentView(self, view):
        self.screenManager.current = view

    def getCurrentView(self):
        return self.screenManager.current