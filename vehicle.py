class Vehicle:
	def __init__(self,registrationNumber,driverAge):
		self.registrationNumber = registrationNumber
		self.driverAge = driverAge

class Car(Vehicle):

	def __init__(self,registrationNumber,driverAge):
		Vehicle.__init__(self,registrationNumber,driverAge)

	def getType(self):
		return "Car"