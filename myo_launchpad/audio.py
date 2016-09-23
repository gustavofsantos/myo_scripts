import winsound
import pygame
import random

class Som:
    def __init__(self, tipo):
        self.tipo     = tipo
        self.tocando  = False
        self.loop     = False
        self.sons = []
        self.som = ""
        self.crescimento = 0
    
    def inicializar(self):
        pygame.mixer.init()
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.init()
        if self.tipo == "bateria1":
            self.sons.append("C:\\Users\\gusta\Documents\\github\\myo_scripts\\myo_launchpad\\sounds\\Urban_pop12a(120BPM).ogg")
            self.sons.append("C:\\Users\\gusta\Documents\\github\\myo_scripts\\myo_launchpad\\sounds\\Urban_pop12b(120BPM).ogg")
            self.sons.append("C:\\Users\\gusta\Documents\\github\\myo_scripts\\myo_launchpad\\sounds\\Urban_pop12c(120BPM).ogg")
            self.sons.append("C:\\Users\\gusta\Documents\\github\\myo_scripts\\myo_launchpad\\sounds\\Urban_pop12d(120BPM).ogg")
        elif self.tipo == "bateria2":
            self.sons.append("C:\\Users\\gusta\Documents\\github\\myo_scripts\\myo_launchpad\\sounds\\Urban_pop02a(92BPM).ogg")
            self.sons.append("C:\\Users\\gusta\Documents\\github\\myo_scripts\\myo_launchpad\\sounds\\Urban_pop02b(92BPM).ogg")
            self.sons.append("C:\\Users\\gusta\Documents\\github\\myo_scripts\\myo_launchpad\\sounds\\Urban_pop02c(92BPM).ogg")
        elif self.tipo == "synt1":
            self.sons.append("C:\\Users\\gusta\Documents\\github\\myo_scripts\\myo_launchpad\\sounds\\Bee_Synt03(130BPM).ogg")
            self.sons.append("C:\\Users\\gusta\Documents\\github\\myo_scripts\\myo_launchpad\\sounds\\Bee_Synt04(130BPM).ogg")
            self.sons.append("C:\\Users\\gusta\Documents\\github\\myo_scripts\\myo_launchpad\\sounds\\Bee_Synt05(130BPM).ogg")
        self.som = self.sons[0]

    def tocar(self):
        print("[Som] Tocando: {}".format(self.som))
        winsound.PlaySound(self.som, SND_FILENAME)

    def tocar_loop(self):
        print("[Som] Tocando em loop: {}".format(self.som))
        winsound.PlaySound(self.som, winsound.SND_LOOP | winsound.SND_ASYNC)

    def parar(self):
        print("[Som] Parar o loop.")
        winsound.PlaySound("C:\\Users\\gusta\\Documents\\musicradar-dance-urban-pop-samples\\One_shots\\FX_01.wav", winsound.SND_PURGE)

    def trocar(self):
        self.som = random.choice(self.sons)

    def aumentar(self):
        self.crescimento = self.crescimento + 1 if self.crescimento < (len(self.sons) - 1) else 0
        winsound.PlaySound(self.som, winsound.SND_PURGE)
        self.som = self.sons[self.crescimento]
        self.tocar_loop()

    def diminuir(self):
        self.crescimento = self.crescimento - 1 if self.crescimento > 1 else (len(self.sons) - 1)
        winsound.PlaySound(self.som, winsound.SND_PURGE)
        self.som = self.sons[self.crescimento]
        self.tocar_loop()