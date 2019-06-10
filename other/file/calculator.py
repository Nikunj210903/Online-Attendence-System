import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class gridlayout(GridLayout):
    def calculate(self,calculation):
        if calculation:
            try:
                self.display.text=str(eval(calculation))
            except Exception:
                self.display = "Syntax error"
    
class calcu(App):
    def build(self):
        return gridlayout()

calcu().run()

