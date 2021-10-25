#!/usr/bin/env python

import sensor
from sensor import *

import serial
from serial import *

class AllSensors:
  def __init__(self):
    #open serial port
    self.s = serial.Serial("COM3",115200,timeout=10)
    #load background image
    self.bgnd = PhotoImage(file="bgnd.gif")
    self.label_bgnd=Label(root,image=self.bgnd)
    self.label_bgnd.place(x=0,y=0)
    #add all sensors and indicators
    self.all = []
    self.all.append(BinSensor("b0", "f0.gif" "f1.gif", 32, 32))
    self.all.append(BinSensor("b1", "f0.gif", "f1.gif", 32, 128))
    self.all.append(vBarSensor("a0", 1, 0, 255, 128, 32, 32, 160))
    self.all.append(GridDisplay("t0", 16, -55, 125, 10, 16, 180, 32, 256, 160))
  def set(self,name,val):
    for sens in self.all:
      if(sens.name == name):
        sens.set(val)
        return
  def setline(self,line):
    p=line.split("=")
    if(len(p)==2):
      self.set(p[0], p[1])
  def run(self):
    while(1):
      line=self.s.readline()
      line=line.rstrip()
      #print(line)
      self.setline(line)
      root.update()

a=AllSensors()
a.run()

