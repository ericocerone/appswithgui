
# Desabilita as mensagens de LOG no console
import os
os.environ["KIVY_NO_CONSOLELOG"] = "1"

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class SayHello(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        # Add widgets to window

        # Image widget
        self.window.add_widget(Image(source="logo.png"))

        # Label widget
        self.greeting = Label(text="What's your name?")
        self.window.add_widget(self.greeting)

        # Text input widget
        self.user = TextInput(multiline=False)
        self.window.add_widget(self.user)

        # Button widget
        self.button = Button(text="GREET")
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)
        
        return self.window
    
    def callback(self, instance):
        self.greeting.text = "Hello " + self.user.text + "!"

if __name__ == "__main__":
    SayHello().run()