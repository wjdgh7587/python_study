#plus, minus, times, division, negation, power
#rem

def cal_plus(a=0,b=0):
	return int(a)+int(b)
	
def cal_minus(a=0,b=0):
	return int(a)-int(b)
	
def cal_times(a=1,b=1):
	return int(a)*int(b)
	
def cal_pow(a=1, b=1):
	return int(a) ** int(b)	
	
def cal_div(a=1, b=1):
	
	if (a==0 or b==0):
		return f"Error"
	else:	
		return int(a)/int(b)

def cal_neg(a=0):
	return -int(a)		
		
def cal_reminder(a=1, b=1):
	if (a==0 or b==0):
		return f"Error"
	else:
		return int(a) % int(b)	

	
#plus
print(cal_plus(2,3))
print(cal_plus(2,"3"))
print(cal_plus(4))
print()

#minus
print(cal_minus(4,"3"))
print(cal_minus(4,4))
print(cal_minus(-2))
print()

#times
print(cal_times(3,3))
print(cal_times(3,"3"))
print(cal_times(2))
print()

#power
print(cal_pow(4,4))
print(cal_pow(2,"8"))
print()

#div
print(cal_div(3,0))				
print(cal_div(3,"3"))
print(cal_div(3,3))
print()

#neg
print(cal_neg(3))
print(cal_neg("3"))
print()

#rem
print(cal_reminder(16,"8"))
print(cal_reminder(4,0))
	