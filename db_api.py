# Copyright 2020 Michaela Reardon micher94@bu.edu

# EC 500
# HMU
# Reardon, Michaela
import sys
import time
from hmu_vitals import bp, pulse
from average import running_averages

recent_bp = []
recent_o2 = []
recent_hr = []

new_patient_file = 'newpatient.txt'
f=open(new_patient_file,"+w")
f.write("data point     blood pressure     heart rate\n")

for i in range(0,1000):

	most_recent_bp = bp(3600)[0]
	most_recent_hr = pulse(3600)[0]

	f.write("%d               %s               %d\n" % (i,str(most_recent_bp),most_recent_hr))
	
	# get most recent values
	recent_bp.append(most_recent_bp)
	recent_hr.append(most_recent_hr)



	while len(recent_hr)>5:
		recent_bp.pop(0)
		recent_hr.pop(0)

	print(recent_bp)
	print(recent_hr)

	# AI uses last 5 data points to calculate running average
	running_averages(recent_bp,recent_hr)

	time.sleep(2)