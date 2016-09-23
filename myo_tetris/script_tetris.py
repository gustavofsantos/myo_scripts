# -*- coding utf 8 -*-
import myo as libmyo
import pyautogui
import pygame
from tetris import *

class Listener(libmyo.DeviceListener):
	def __init__(self):
		super(Listener, self).__init__()
		self.orientation = None
		self.pose = libmyo.Pose.rest
		self.emg_enabled = True
		self.locked = False
		self.rssi = None
		self.emg = None
		self.last_time = 0

	def on_pair(self, myo, timestamp, firmware_version):
		print("Myo conectada!")

	def on_unpair(self, myo, timestamp):
		print("Myo desconectada!")

	def on_lock(self, myo, timestamp):
		self.locked = True
		print('Lock')

	def on_unlock(self, myo, timestamp):
		self.locked = False
		print('Unlock')

	def on_pose(self, myo, timestamp, pose):
		if pose == libmyo.Pose.fist:
			print('[*] Punho fechado')
			pygame.event.post(pygame.event.Event(pygame.KEYDOWN))
		elif pose == libmyo.Pose.double_tap:
			print('[*] Toque duplo')
		elif pose == libmyo.Pose.wave_out:
			print('[*] Wave out')
			pygame.event.post(pygame.event.Event(pygame.K_RIGHT))
		elif pose == libmyo.Pose.wave_in:
			print('[*] Wave in')
			pygame.event.post(pygame.event.Event(pygame.K_LEFT))
		elif pose == libmyo.Pose.fingers_spread:
			print('[*] Mao aberta')
			pygame.event.post(pygame.K_p)


def main():
	# pyautogui.PAUSE = 1
	pyautogui.FAILSAFE = True
	libmyo.init('C:\\myo-sdk-win-0.9.0\\bin')
	hub = libmyo.Hub()
	hub.run(1000, Listener())
	try:
		print('Pressione Ctrl+C para sair.')
		App = TetrisApp()
		App.run()
		while True:
			pass
	except KeyboardInterrupt:
		print('Saindo...')
	finally:
		hub.shutdown()


if __name__ == '__main__':
	main()
