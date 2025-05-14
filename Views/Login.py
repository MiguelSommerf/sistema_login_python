from kivymd.uix.screen import MDScreen
from kivy.config import Config
Config.set('graphics', 'borderless', True)  # Remove the title bar

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout

KV = '''
MDScreen:
    md_bg_color: 43/255, 45/255, 66/255, 1  # Set the background color of the screen (light gray)
    

    MDIconButton:
        order: 1
        icon: "close"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1  # White Icon
        on_release: app.stop()  # Close the application
    

    MDBoxLayout:
        orientation: "vertical"
        spacing: dp(20)
        padding: dp(20)
        size_hint: None, None
        size: dp(300), dp(400)
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        md_bg_color: 237/255, 242/255, 244/255, 0.4  # Converted RGBA to normalized values
        radius: [10, 10, 10, 10]  # Rounded corners

        

        MDLabel:
            text: "Entrar"
            font_style: "H4"
            halign: "center"
            size_hint_y: None
            color: 1, 1, 1, 1
            height: self.texture_size[1]

        MDTextField:
            id: email_field
            hint_text: "Email"
            icon_left: "email"
            icon_left_color_normal: 1, 1, 1, 1
            icon_left_color_focus: 0.1686, 0.1765, 0.2588, 1
            mode: "line"
            hint_text_color_normal: 1, 1, 1, 1
            hint_text_color_focus: 0.1686, 0.1765, 0.2588, 1
            helper_text: "Digite seu email"
            line_color_normal: 1, 1, 1, 1
            line_color_focus: 1, 1, 1, 1 
            helper_text_color_focus: 1, 1, 1, 1

        MDTextField:
            id: password_field
            hint_text: "Senha"
            icon_left: "lock"
            icon_left_color_focus: 0.1686, 0.1765, 0.2588, 1
            icon_left_color_normal: 1, 1, 1, 1
            hint_text_color_normal: 1, 1, 1, 1
            hint_text_color_focus: 0.1686, 0.1765, 0.2588, 1
            text_color: 1, 1, 1, 1
            line_color_normal: 1, 1, 1, 1
            line_color_focus: 1, 1, 1, 1
            helper_text: "Digite sua senha"
            helper_text_color_focus: 1, 1, 1, 1
            password: True
            mode: "line"

        MDBoxLayout:
            orientation: "horizontal"
            spacing: dp(100)
            size_hint_y: None
            height: dp(50)

            MDRaisedButton:
                text: "Cadastrar"
                md_bg_color: 216/255, 0/255, 50/255, 1  # Converted RGBA to normalized values
                text_color: 1, 1, 1, 1

            MDRaisedButton:
                text: "Entrar"
                md_bg_color: 239/255, 35/255, 60/255, 1
                text_color: 1, 1, 1, 1
                on_release: app.root.controller.userController.logginUser(email_field.text, password_field.text)  # Call the logginUser method


'''

class LoginScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        layout = Builder.load_string(KV)
        self.add_widget(layout)