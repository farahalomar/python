from datetime import datetime
class Employee:
	date = datetime.now()
	today_year = date.year
	def __init__(self,name,age,salary,employment_date):
		self.name = name
		self.age = age
		self.salary = salary
		self.employment_date = employment_date
	
	def get_working_years(self):
		return (self.today_year - self.employment_date)
class Manager(Employee):

	def __init__(self,name,age,salary,employment_date,bonus_percentage):
		Employee.__init__(self,name,age,salary,employment_date)
		self.bonus_percentage = bonus_percentage

	def get_bonus(self):
		return (self.bonus_percentage * self.salary)
employees = []
managers = []
print ("    Welcome to HR Pro 2019")
while True:
	print ("    Choose an action to do:")
	print ("        1. show employees")
	print ("        2. show managers")
	print ("        3. add an employee")
	print ("        4. add a manager")
	print ("        5. exit \n ")
	action = int(raw_input("what would you like to do? "))
	if (action == 1):
		if len(employees) == 0:			
			print("-----------------")
			print("The list is empty, please add an employee to show results!")
			print("----------------- \n")
		else:
			for emplist in employees:				
				print("-----------------")
				print("Employees")
				print("name: " + emplist.name + ", " + "age: " + str(emplist.age) + ", " + "salary: " + str(emplist.salary) + ", " 
					+ "working years: " + str(emplist.get_working_years()) + "\n" )
				print("----------------- \n")
	elif (action == 2):
		if len(managers) == 0:			
			print("-----------------")
			print("The list is empty, please add an manager to show results!")
			print("----------------- \n")
		else:
			for mnglist in managers:				
				print("-----------------")
				print("Managers")
				print("name: " + mnglist.name + ", " + "age: " + str(mnglist.age) + ", " + "salary: " + str(mnglist.salary) + ", " 
					+ "working years: " + str(mnglist.get_working_years()) + ", " + "bonus: " + str(mnglist.get_bonus()) + "\n" )
				print("----------------- \n")
	elif (action == 3):
		e_name = raw_input("name: ")
		e_age = int(raw_input("age: "))
		e_salary = int(raw_input("salary: "))
		e_year = int(raw_input("employement year: "))
		employee = Employee(e_name, e_age, e_salary, e_year)
		employees.append(employee)		
		print("-----------------")
		print ("Employee added succesfully \n")
	elif (action == 4):
		m_name = raw_input("name: ")
		m_age = int(raw_input("age: "))
		m_salary = int(input("salary: "))
		m_year = int(raw_input("employement year: "))
		m_bonus = float(raw_input("bonus percentage: "))
		manger = Manager(m_name, m_age, m_salary, m_year, m_bonus)
		managers.append(manger)
		print("-----------------")
		print ("Employee added succesfully \n")
	elif (action == 5):
		break
	else:
		print("Action not available! .. please select from 1 to 5.")
