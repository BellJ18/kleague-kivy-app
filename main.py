from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class KLeagueApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        label = Label(text='K리그 일정 알리미 앱입니다!')
        button = Button(text='확인')
        layout.add_widget(label)
        layout.add_widget(button)
        return layout

KLeagueApp().run()
