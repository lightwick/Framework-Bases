from kivy.uix.widget import Widget
from kivy.app import App
from kivy.core.window import Window

class CanvasWidget(Widget): 
    def __init__(self, **kwargs): 
  
        super(CanvasWidget, self).__init__(**kwargs) 
  
        # Arranging Canvas 
        with self.canvas: 
  
            Color(.234, .456, .678, .8)  # set the colour  
  
            # Seting the size and position of canvas 
            self.rect = Rectangle(pos = self.center, 
                                  size =(self.width / 2., 
                                        self.height / 2.)) 
  
            # Update the canvas as the screen size change 
            self.bind(pos = self.update_rect, 
            size = self.update_rect) 
  
    # update function which makes the canvas adjustable.
    
    def update_rect(self, *args): 
        self.rect.pos = self.pos 
        self.rect.size = self.size
        
class myApp(App):
    def build(self):
        game = Widget()
        return game
    def on_stop(self):
        Window.close()
        
if __name__ == "__main__":
    myApp().run()
        
