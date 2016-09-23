#!python3
# -*- coding utf-8 -*-

import myo as libmyo
import sons
import pygame

#cd Documents\github\myo_scripts\myo_launchpadpy

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
        self.channel_bateria = None
        self.channel_synt = None
        self.select_bateria = 0
        self.select_synt = 0
        print("[!] Canais criados")
        self.tocando_bateria = False
        self.tocando_synth = False
        

    def on_pair(self, myo, timestamp, firmware_version):
        pygame.mixer.init()
        pygame.mixer.pre_init(frequency = 44100, size = -16, channels = 1, buffer = 2**12)
        pygame.init()
        self.channel_bateria = pygame.mixer.Channel(0)
        self.channel_synt = pygame.mixer.Channel(1)
        print("[!] Myo conectada!")

    def on_unpair(self, myo, timestamp):
        print("[!] Myo desconectada!")

    def on_lock(self, myo, timestamp):
        self.locked = True
        print('[*] Travado')

    def on_unlock(self, myo, timestamp):
        self.locked = False
        print('[*] Destravado')

    def on_arm_sync(myo, timestamp, arm, x_direction, rotation, warmup_state):
        print(rotarion)

    def on_pose(self, myo, timestamp, pose):
        if pose == libmyo.Pose.fist:
            print('[*] Punho fechado')
            if not self.tocando_bateria:
                self.channel_bateria.play(pygame.mixer.Sound(sons.bateria_a1[self.select_bateria]), loops=-1)
                self.tocando_bateria = True
            else:
                self.channel_bateria.stop()
                self.tocando_bateria = False
        elif pose == libmyo.Pose.double_tap:
            print('[*] Toque duplo')
            if not self.tocando_synth:
                self.channel_synt.play(pygame.mixer.Sound(sons.synt_a3_92), loops=-1)
                self.tocando_synth = True
            else:
                self.channel_synt.stop()
                self.tocando_synth = False
        elif pose == libmyo.Pose.wave_out:
            print('[*] Wave out')
            self.select_bateria = self.select_bateria + 1 if self.select_bateria < len(sons.bateria_a1) + 1 else 0
            self.channel_bateria.play(pygame.mixer.Sound(sons.bateria_a1[self.select_bateria]), loops=-1)
        elif pose == libmyo.Pose.wave_in:
            print('[*] Wave in')
            self.select_bateria = self.select_bateria - 1 if self.select_bateria > 1 else len(sons.bateria_a1) - 1
            self.channel_bateria.play(pygame.mixer.Sound(sons.bateria_a1[self.select_bateria]), loops=-1)
        elif pose == libmyo.Pose.fingers_spread:
            print('[*] Mão aberta')

def main():
    libmyo.init('C:\\myo-sdk-win-0.9.0\\bin')
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
    import sys
    sys.exit(int(main() or 0))