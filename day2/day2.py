#def test_python(who="anonymous"):
#	print("Hello", who)
#	
#test_python("JH")
#test_python()
#
#def test_number(a,b):
#	print(a+b)
#	print(a*b)
#def test_minus(a,b):
#	print(a-b)	
#	
#test_number(4, 3)
#test_minus(4, 6)

#positional argument
#we dont have to care about the argument position
#that is fuxking awesome

#def p_plus(a,b):
#	print(a+b)
#	
#def r_plus(a,b):
#	return a+b
#	
#p_result = p_plus(2, 3)
#r_result = r_plus(2, 3)
#
#print(p_result, r_result)		

def say_hello(name, age):
	return f"Hello {name} you are {age} years old"
		
hello = say_hello("JH", "12")
print(hello)		

def say_hello(name, age):
	return "Hello" + name + "you are"+ age +"years old"
		
hello = say_hello("JH", "12")
print(hello)		