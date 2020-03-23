# -*- coding: utf-8 -*-
# Author: Pat Rick Ntwari
# Assignment 6
# EC500
# Prof. Osama A. 

# This code produces random numbers intended to simulate the vitals of a human being
# These vitals are: blood pressure and pulse

import random
from bp_range import sysranges, diaranges

# will take in the sec interval data is required. for example: if data is required every 1 sec
# then sec = 1;
# returned data will be a list of hour-equivalent data in tuple form;
# that is for sec=1; the list will be 3600 tuples

def bp(sec):
  # establish boundaries for blood pressure
  bpmin_sys = 90
  bpmax_sys = 180

  hour = 3600    # 1 hr = 3600 seconds 
  listsize = hour//sec

  #initialize lists
  bp =[]
  
  for i in range(0,listsize):
    if not bp:
      bp_sys = random.randrange(bpmin_sys, bpmax_sys)
      bp_dia = dia(bp_sys)
    else: 
      #bp_sys = random.randrange(bp[i-1][0]-(bp[i-1][0]*0.1), bp[i-1][0]+(bp[i-1][0]*0.1))

      # THis is to ensure the consecutive blood pressures are at least close to each other. 
      # so they dont go from 110 to 85 
      if bp[i-1][0]-5 < bpmin_sys:
        rangebot = bpmin_sys
      else:
        rangebot = bp[i-1][0]-5
      if bp[i-1][0]+5 > bpmax_sys:
        rangetop = bpmax_sys
      else:
        rangetop = bp[i-1][0]+5

      bp_sys = random.randrange(rangebot, rangetop)
      bp_dia = dia(bp_sys)

    bp_tup = (bp_sys, bp_dia)

    bp.append(bp_tup)

  return bp

# Only called by bp
def dia(bp_sys):
  print(" bp sys ", bp_sys)
  sys_ranges = sysranges()
  dia_ranges = diaranges()
  if bp_sys in sys_ranges[0]:
    bp_dia = random.randrange(40,60)
  if bp_sys in sys_ranges[1]:
    bp_dia = random.randrange(60,65)
  if bp_sys in sys_ranges[2]:
    bp_dia = random.randrange(65,70)
  if bp_sys in sys_ranges[3]:
    bp_dia = random.randrange(70,80)
  if bp_sys in sys_ranges[4]:
    bp_dia = random.randrange(80,85)
  if bp_sys in sys_ranges[5]:
    bp_dia = random.randrange(85,90)
  if bp_sys in sys_ranges[6]:
    bp_dia = random.randrange(90,95)
  if bp_sys in sys_ranges[7]:
    bp_dia = random.randrange(95,100)
  if bp_sys in sys_ranges[8]:
    bp_dia = random.randrange(100,110)
  return bp_dia

# CAll pulse the same way as bp. Give the time step for data. If data is needed for each 1 second,
# sec should equal 1 and the list of pulses will be size 3600
def pulse(sec):
  pulse_min = 60
  pulse_max = 100

  hour = 3600
  listsize = hour//sec

  # initialize list
  pulse = []

  for i in range(0,listsize):
    if not pulse:
      res = random.randrange(pulse_min, pulse_max)
    else: 
      if pulse[i-1]-5<pulse_min:
        rangebot = pulse_min
      else:
        rangebot = pulse[i-1]-5
      if pulse[i-1]+5>pulse_max:
        rangetop = pulse_max 
      else:
        rangetop = pulse[i-1]+5

      res = random.randrange(rangebot, rangetop)  
    pulse.append(res)
  
  return pulse

def main():
  scale = 180
  print(bp(scale))
  print(pulse(scale))


if __name__ == '__main__':
  main()