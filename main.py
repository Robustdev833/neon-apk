
# main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Line
from kivy.clock import Clock
from kivy.core.window import Window
import random

Window.clearcolor = (0.02, 0.02, 0.05, 1)  # Very dark background

class FuturisticBackground(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.draw_network, 0.1)

    def draw_network(self, dt):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0, 1, 1, 0.2)  # Light neon cyan
            for _ in range(25):
                x1 = random.randint(0, Window.width)
                y1 = random.randint(0, Window.height)
                x2 = x1 + random.randint(-40, 40)
                y2 = y1 + random.randint(-40, 40)
                Line(points=[x1, y1, x2, y2], width=1.2)

class NeonCalcApp(App):
    def build(self):
        self.expr = ""
        root = FuturisticBackground(orientation='vertical', padding=10, spacing=10)

        self.display = TextInput(text="", font_size=32, readonly=True, halign="right",
                                 size_hint=(1, 0.2), foreground_color=(0, 1, 1, 1),
                                 background_color=(0, 0, 0, 0.3), cursor_color=(0, 1, 1, 1),
                                 font_name="Roboto")
        root.add_widget(self.display)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['.', '0', '=', '+'],
            ['C', '⌫']
        ]

        for row in buttons:
            h_box = BoxLayout(size_hint=(1, 0.15), spacing=5)
            for label in row:
                btn = Button(text=label, font_size=24, font_name="Roboto",
                             background_normal='',
                             background_color=(0.0, 0.6, 0.8, 0.7),
                             color=(0, 1, 1, 1))
                btn.bind(on_release=self.on_button_press)
                h_box.add_widget(btn)
            root.add_widget(h_box)

        credit = Label(text="Developer: Farhan Wani", font_size=14, size_hint=(1, 0.05),
                       color=(0, 1, 1, 0.7), font_name="Roboto")
        root.add_widget(credit)

        return root

    def on_button_press(self, instance):
        text = instance.text
        if text == 'C':
            self.expr = ""
        elif text == '⌫':
            self.expr = self.expr[:-1]
        elif text == '=':
            try:
                self.expr = str(eval(self.expr))
            except:
                self.expr = 'Error'
        else:
            self.expr += text
        self.display.text = self.expr

if __name__ == '__main__':
    NeonCalcApp().run()
