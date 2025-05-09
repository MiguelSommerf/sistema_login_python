# GPT Code for testing Kivy. We won't use this code in the final version.
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel


class LoginApp(MDApp):
    
    def build(self):
        self.screen = Screen()

        # E-mail Field
        self.email = MDTextField(
            hint_text="Email",
            pos_hint={"center_x": 0.5, "center_y": 0.6},
            size_hint_x=0.8
        )
        self.screen.add_widget(self.email)

        # Password Field
        self.password = MDTextField(
            hint_text="Password",
            password=True,
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            size_hint_x=0.8
        )
        self.screen.add_widget(self.password)

        # Login Button
        login_button = MDRaisedButton(
            text="Login",
            pos_hint={"center_x": 0.5, "center_y": 0.4},
            on_release=self.check_credentials  # <- chamada aqui
        )
        self.screen.add_widget(login_button)

        # Result Label
        self.result_label = MDLabel(
            text="",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.3}
        )
        self.screen.add_widget(self.result_label)

        return self.screen

    def check_credentials(self, instance):
        email = self.email.text
        password = self.password.text

        return self.screen
    
if __name__ == "__main__":
    LoginApp().run()