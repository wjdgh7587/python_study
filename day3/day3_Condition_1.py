#def plus(a,b):
#	#if user gave me a string(CONDITION MUBS BE HERE)
#	#error
#	#else
#	#return a+b
#	if type(b) is int or type(b) is float:
#		return a+b
#	else:
#		return None
#		
#r_plus = plus(12, 1.2)
#print(r_plus)	

#Truth value testing find in docset	

#Boolean Operations OR, AND, NOT
#IF ,elif, else

def age_check(age):
	print(f"You are {age}")
	if age<18:
		print("You cant drink")
	elif age == 18 or age == 19: #else if
		print("You are new to this!!")	
	elif age>20 and age < 25:
		print("You are still kind of young")	
	else:
		print("enjoy your drink")	
	
age_check(23)	
