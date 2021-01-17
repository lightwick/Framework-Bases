from kivy.uix.widget import Widget
from kivy.app import App
from kivy.core.window import Window

class myApp(App):
    def build(self):
        game = Widget()
        return game
    def on_stop(self):
        Window.close()
        
if __name__ == "__main__":
    myApp().run()
        
