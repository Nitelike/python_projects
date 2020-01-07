from random import random
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line, Ellipse
from kivy.core.window import Window

class CustomInput(TextInput):
    def on_text(self, *kwargs):
        Parent.name = self.text

class Parent(BoxLayout):
    name = ''

    def save(self, *kwargs):
        self.popup.dismiss()
        painter = self.ids['painter']
        painter.export_to_png(Parent.name)

    def custom_popup(self):
        box = BoxLayout(orientation = 'vertical', padding = (10))
        t = CustomInput(text = "test.png", size_hint_y = 2, multiline=False)
        Parent.name = t.text
        box.add_widget(t)
        box.add_widget(Widget(size_hint_y = 8))
        self.popup = Popup(title='Saving',
                      title_align = 'center', content = box,
                      size_hint=(None, None), size=(400, 400),
                      auto_dismiss = True)
        box.add_widget(Button(text = "Save", size_hint_y = 2, on_release = self.save))

        self.popup.open()

class PaintWidget(Widget):
    color = [0, 0, 0, 1]
    w = 4

    def on_touch_down(self, touch):
        with self.canvas:
            Color(*PaintWidget.color)
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=PaintWidget.w)
            Ellipse(pos=(touch.x - 2*PaintWidget.w / 2, touch.y - 2*PaintWidget.w / 2), size=(2*PaintWidget.w, 2*PaintWidget.w))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]
        PaintApp.picture = touch.ud['line']

    def set_color(self, color):
        PaintWidget.color = color

class PaintApp(App):
    picture = []
    Window.clearcolor = (1, 1, 1, 1)
    def build(self):
        return Parent()

if __name__ == '__main__':
    PaintApp().run()
