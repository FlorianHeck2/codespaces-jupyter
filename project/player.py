import pygame
import sys
class spieler:
    def __init__(self,x,y,geschw,breite,hoehe,richtg,schritteLinks,schritteRechts):
        self.x = x
        self.y = y
        self.geschw = geschw
        self.breite = breite
        self.hoehe = hoehe
        self.richtg = richtg
        self.schritteLinks = schritteLinks
        self.schritteRechts = schritteRechts
        self.last = [1,0]
        self.ok = True        