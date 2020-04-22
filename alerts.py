# Copyright 2020 erinkate@bu.edu
# EC500

from hmu_vitals import bp, pulse


def alert(bp, pulse):
  alert = False
  if bp[0] > 180: 
  	alert = True
  if bp[1] > 110:
  	alert = True
  if pulse > 72:
  	alert = True
  return alert
