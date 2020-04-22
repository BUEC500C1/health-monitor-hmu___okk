# -*- coding: utf-8 -*-
# Author: Pat Rick Ntwari
# Assignment 6
# EC500
# Prof. Osama A. 

# This code displays some vitals such as pulse and blood pressure of patient

from hmu_vitals import bp, pulse
from alerts import alert
import time
from datetime import datetime, date


def display(sec):
  bloodp = bp(sec)
  #print("got bp")
  heartp = pulse(sec)
  # print("length of pulse ", len(bloodp))
  today = date.today()

  dispsec = 5
  
  ## must give a time interval lower than 10
  if sec > 5:
    print("Your second interval should be less than 5")
  
  else:
    print("************************VITALS*************************")
    print("****************DATE: ", today, " *********************")
    #for i in range(0,len(bloodp),dispsec):
    for i in range(0, 25):
      now = datetime.now()
      tf = now.strftime("%H:%M:%S")
      print(tf, "  Blood Pressure  ", bloodp[i][0], " / ", bloodp[i][1])
      print(tf, "  Pulse ", heartp[i])
      time.sleep(dispsec)
      if alert(bloodp[i], heartp[i]) == True: 
        print(tf, "  CHECK PATIENT VITALS, ALERT CONDITION FOUND")


def main():
  sec = 1
  display(sec)



if __name__ == '__main__':
  main()