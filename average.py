def running_averages(recent_bp,recent_hr):
	#parse blood pressure list
	dia = []
	sys = []
	hr = []

	for i in range(0,len(recent_bp)):
		bp = recent_bp[i]
		dia.append(bp[0])
		sys.append(bp[1])
		hr.append(recent_hr[i])

	dia_sum = 0
	for i in range(0,len(dia)):
		dia_sum = dia_sum + dia[i]
	dia_avg = dia_sum/len(dia)
	round(dia_avg,2)
	print('average diastolic pressure is ', dia_avg)

	sys_sum = 0
	for i in range(0,len(sys)):
		sys_sum = sys_sum + sys[i]
	sys_avg = sys_sum/len(sys)
	round(sys_avg,2)

	print('average systolic pressure is ', sys_avg)

	hr_sum = 0
	for i in range(0,len(hr)):
		hr_sum = hr_sum + hr[i]
	hr_avg = hr_sum/len(hr)
	round(hr_avg,2)

	print('average heart rate is ', hr_avg)