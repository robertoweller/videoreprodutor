import kivy
kivy.require('1.10.1')
from kivy.uix.videoplayer import VideoPlayer
from kivy.app import App

class rodaVideo(App):
	def build(self):
		# precisa ser estudado mais essa classe, mas gostie muito.
		# Carrega o local do video e carrega a classe video 
		self.video = VideoPlayer(source = 'lind-musi-anime.mp4')

		return self.video # Retorna 'chama' o video e a variavel que contem a class VideoPlayer()

if __name__ == '__main__':
	# Da o estart no app, começa o loop.
	rodaVideo().run() 
