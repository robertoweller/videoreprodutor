import kivy
kivy.require('1.10.1')
from kivy.uix.videoplayer import VideoPlayer
from kivy.app import App

class rodaVideo(App):
	def build(self):
		# Carrega o local do video e carrega a classe video 
		self.video = VideoPlayer(source = 'lind-musi-anime.mp4')

		return self.video # Retorna 'chama' o video e a variavel que contem a class VideoPlayer()

if __name__ == '__main__':
	# Da o estart no app, roda a bagaça, pelo app retornar o video carrega o priprio
	rodaVideo().run() 
