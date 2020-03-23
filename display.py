# -*- coding: utf-8 -*-
# Author: Pat Rick Ntwari
# Assignment 6
# EC500
# Prof. Osama A. 

# This code displays some vitals such as pulse and blood pressure of patient

from hmu_vitals import bp, pulse
import time
from datetime import datetime, date


def display(sec):
  bloodp = bp(sec)
  heartp = pulse(sec)

  today = date.today()

  dispsec = 5
  
  ## must give a time interval lower than 10
  if sec > 5:
    print("Your second interval should be less than 10")
  
  else:
    print("************************VITALS*************************")
    print("****************DATE: ", today, " *********************")
    for i in range(0,len(bloodp),dispsec):
      now = datetime.now()
      tf = now.strftime("%H:%M:%S")
      print(tf, "  Blood Pressure  ", bloodp[i][0], " / ", bloodp[i][1])
      print(tf, "  Pulse ", heartp[i])
      time.sleep(dispsec)


def main():
  sec = 1
  display(sec)



if __name__ == '__main__':
  main()