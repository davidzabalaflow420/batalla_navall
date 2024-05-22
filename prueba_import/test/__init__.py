from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class Tablero(GridLayout):
    def __init__(self, **kwargs):
        super(Tablero, self).__init__(**kwargs)
        self.cols = 8
        self.rows = 8
        self.buttons = []
        for row in range(8):
            for col in range(8):
                button = Button(text=' ', font_size=40, size_hint=(None, None), width=100, height=100)
                button.bind(on_press=self.on_button_click)
                self.add_widget(button)
                self.buttons.append(button)

    def on_button_click(self, instance):
        if instance.text == ' ':
            instance.text = 'X'
        else:
            instance.text = ' '

class TicTacToeApp(App):
    def build(self):
        return Tablero()

if __name__ == '__main__':
    TicTacToeApp().run()
