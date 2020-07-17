import os
import requests

def check_url():
	url_input = input("Welcom to IsitDown.py!\nPlease write a URL or URLs you want to check. (separated by comma)\n")

	#Separating Func split() with lowercase
	url_index = []
	url_input=url_input.lower()
	url_input=url_input.replace(" ", "")
	url_split_r=url_input.split(",")

	#Append URL Func
	for upload_url in url_split_r:
		url_index.append(upload_url)    

	#Main Func
	try:
		for lookfor_url in url_index:
			if "." in lookfor_url:
				try:
					r=requests.get(f"https://{lookfor_url}")
					if r.status_code == 200:
						print(f"https://{lookfor_url} is up!")
				except:  
						print(f"https://{lookfor_url} is down!")
			else:
				if "http://" in lookfor_url:
					try:
						r=requests.get(f"{lookfor_url}")
						if r.status_code == 200:
							print(f"{lookfor_url} is up!")         
					except:  
						print(f"{lookfor_url} is down!")          
		ask_opinion()        
	except:
		print(f"{lookfor_url} is not valied URL.")
		ask_opinion()
		

			
###### Ask opinion ############
def ask_opinion():
	recheck_opinion = input("Do you want to start over? Y/N\n")

	recheck_opinion = recheck_opinion.upper()

	if recheck_opinion == "Y":
		os.system('clear')
		check_url()

	elif recheck_opinion == "N":
		print("OK, Bye")
		SystemExit 
	else:
		print(f"{recheck_opinion} is not valied Order")
 
check_url()

#################################
#Conclusion
#Split(), replace(), strip(), requests
#status_code == 200
#######################################
#
# "The right example
#
########################################
#import os
#import requests
#
#def restart():
#	answer = str(input("Do you want to start over? y/n ")).lower()
#	if answer == "y" or answer =="n":
#		if answer == "n":
#				print("k. bye!")
#				return
#		elif answer == "y":
#			main()
#	else:
#		print("That's not a valid answer")
#		restart()
#
#
#def main():
#	os.system('clear')
#	print("Welcome to IsItDown.py!\nPlease write a URL or URLs you want to check. (separated by comma)")
#	urls = str(input()).lower().split(",")
#	for url in urls:
#		url = url.strip()
#		if "." not in url:
#			print(url, "is not a valid URL.")
#		else:
#			if "http" not in url:
#				url = f"http://{url}"
#			try:
#				request = requests.get(url)
#				if request.status_code == 200:
#					print(url,"is up!")
#				else:
#					print(url, "is down!")
#			except:
#					print(url, "is down!")
#	restart()
#
#
#main()