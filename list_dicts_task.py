print("Welcome to The Special Recruitment Program, please answer the following questions:\n")
skills=["python","c++","javascript","juggling","running","eating"]

cv={}

cv["name"]=raw_input("Name: ").title()
cv["age"]=int(raw_input("Age: "))
cv["experience"]=int(raw_input("How many years of experience do you have? "))
cv["skills"]=[]

print("skills:\n1- "+skills[0]+"\n2- "+skills[1]+"\n3- "+skills[2]+"\n4- "+skills[3]+"\n5- "+skills[4]+"\n6- "+skills[5])
cv["skills"]=[skills[int(raw_input("Type in the number of the skill you acquire from the skills above : "))-1],skills[int(raw_input("Choose another skills from above: "))-1]]

if ("python" in cv["skills"] or "c++" in cv["skills"]) and cv["age"]>=21 and cv["age"]<=29 and cv["experience"]>=0 and cv["experience"]<=3:
	print("Congratulations "+cv["name"]+", your application have been accepted!")
else:
	print("We regret to inform you that your application has not been accepted "+cv["name"]+".")
