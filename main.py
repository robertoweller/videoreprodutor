#import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.label import Label


class tela(BoxLayout):
	pass


class main(App):
	def build(self):
		return tela()

programa = main()

programa.run()





