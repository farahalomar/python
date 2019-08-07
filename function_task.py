from datetime import date

def check_birthdate(day, month,year):
	if year > date.today().year:
		return False
	elif year == date.today().year:
		if month > date.today().month:
			return False
		elif month == date.today().month:
			if day > date.today().day:
				return False
			elif day < 0:
				return False
			else:
				return True
		elif month < 0 or day < 0 or day > 31:
			return False
		else:
			return True
	elif year < 0 or month > 12 or month < 0 or day < 0 or day > 31:
		return False
	else:
		return True	
def calculate_age(day, month, year):
	y_age = date.today().year - year
	m_age = date.today().month - month
	d_age = date.today().day - day

	print("Your age is %s years, %s months and %s days."%(y_age, m_age, d_age))
	
year = int(input("Enter the year you were born in: "))
month = int(input("Enter the month you were born in: "))
day = int(input("Enter the day you were born in: "))

if check_birthdate(day, month, year) == True:
	calculate_age(day, month, year)
else:
	print("This birthday is innaccurate")
