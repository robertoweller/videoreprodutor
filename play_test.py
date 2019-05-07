import kivy
kivy.require('1.9.0')
from kivy.uix.videoplayer import VideoPlayer
from kivy.app import App

class rodaVideo(App):
	def build(self):
		# Carrega o local do video e carrega a classe video 
		self.video = VideoPlayer(source = 'caminho_do_video/video.mp4')

		return self.video # Retorna 'chama' o video a propriedade que ta a class Video()

if __name__ == '__main__':
	# Da o estart no app, roda a bagaça, pelo app retornar o video carrega o priprio
	rodaVideo().run() 
