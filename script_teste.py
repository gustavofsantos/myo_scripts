import time
import myo as libmyo
import pyautogui


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
		self.largura = pyautogui.size()[0]
		self.altura = pyautogui.size()[1]

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

	def on_accelerometor_data(self, myo, timestamp, acceleration):
		print('acelerometro')
		print(acceleration)

	def on_orientation_data(self, myo, timestamp, orientation):
		print('orientação')
		print(orientation)
		'''
		x0, y0 = pyautogui.position()
		dx = orientation.x
		dy = orientation.y
		x = x0 -10*(dx)
		y = y0 -10*(dy)
		pyautogui.moveTo(x, y)
		'''

	# print("Orientation:", orientation.x, orientation.y, orientation.z, orientation.w)

	def on_gyroscope_data(self, myo, timestamp, gyroscope):
		print('giroscopio')
		x, y = pyautogui.position()
		data_x = gyroscope[0]
		data_y = gyroscope[1]
		print(gyroscope)
		print(data_x)
		print(data_y)
		move_x = x + 10*(data_x)
		move_y = y + 10*(data_y)
		if move_x > 0 and move_y > 0:
			if move_y <= self.altura and move_x <= self.largura:
				pyautogui.moveTo(x + data_x, y + data_y)
			else:
				print('[-] Fora do limite da tela')
		else:
			print('[-] Fora do limite da tela')

	def on_pose(self, myo, timestamp, pose):
		if pose == libmyo.Pose.fist:
			print('[*] Punho fechado')
			pyautogui.click(button='right')
		elif pose == libmyo.Pose.double_tap:
			print('[*] Toque duplo')
			pyautogui.click(button='left')


def main():
	# pyautogui.PAUSE = 1
	pyautogui.FAILSAFE = True
	libmyo.init('C:\\myo-sdk-win-0.9.0\\myo-sdk-win-0.9.0\\bin')
	hub = libmyo.Hub()
	hub.run(1000, Listener())
	try:
		print('Pressione Ctrl+C para sair.')
		while True:
			pass
	except KeyboardInterrupt:
		print('Saindo...')
	finally:
		hub.shutdown()


if __name__ == '__main__':
	main()
