
class Alert(object):
	"""docstring for ClassName"""
	def __init__(self, patient="000", systolic=120, diatolic=80, pulse=60, O2=95):
		self.patient = patient
		self.systolic = systolic
		self.diatolic = diatolic
		self.pulse = pulse
		self.O2 = O2

	def __str__(self):
		result = "Patient "+ self.patient + "\nSystolic: " + str(self.systolic) + " Diatolic: " + str(self.diatolic) + "\nPulse: " + str(self.pulse) + "\nO2: " + str(self.O2) + "\n"
		return result

	def __repr__(self):
		result = "Patient "+ self.patient + "\nSystolic: " + str(self.systolic) + " Diatolic: " + str(self.diatolic) + "\nPulse: " + str(self.pulse) + "\nO2: " + str(self.O2) + "\n"
		return result

	def check_BP(self):
		# Hypertensive crisis
		if self.systolic >= 140 or self.diatolic >= 90:
			print("Hypertensive Crisis")
			return True
		# High blood pressure
		elif self.systolic >=130 or self.diatolic >= 80:
			print("High Blood Pressure")
			return True
		# Elevated
		elif self.systolic>=120 and self.diatolic < 80:
			print("Elevated Blood Pressure")
			return True
		return False

	def check_pulse(self):
		if self.pulse > 100:
			print("High Pulse")
			return True
		elif self.pulse <= 55:
			print("Low Pulse")
			return True
		return False

	def check_O2(self):
		if self.O2 <95:
			print("Low Blood Oxygen")
			return True
		return False

	def result(self):
		self.check_BP()
		self.check_pulse()
		self.check_O2()
		if self.check_BP or self.check_pulse or self.check_O2:
			print(self)


if __name__ == "__main__":
	patients = []
	systolics = []
	diatolics = []
	pulses = []
	O2s = []

	f = open("sample.txt","r+")
	f.readline()
	for line in f:
		info = line.split()
		patients.append(info[0])
		systolics.append(int(info[1]))
		diatolics.append(int(info[2]))
		pulses.append(int(info[3]))
		O2s.append(int(info[4]))

	f.close()

	for i in range(0,len(patients)):
		s = Alert(patients[i], systolics[i],diatolics[i], pulses[i],O2s[i])
		s.result()
