from Check_Proxies import Check_Proxies
from os import system
from library import SleepD
def Get_input(String : str, Type: type) -> type:
	while True:
		try:
			TEMP = input(String)
			if TEMP == "":
				return None
			return Type(TEMP)
		except ValueError:
			print("Wrong Type! Try again")
			SleepD(3)
			system("cls")
			system("title  ")



if __name__ == "__main__":
	system("cls")
	system("title Proxy Checker V_1.0")

	#Gets Server
	Server = Get_input("Please Enter The Server (Defaults to Google.com): ", str)
	if not Server:
		Server = "Google.com"
	system("title Proxy Checker V_1.0")


	#Gets Proxy Filename
	Proxy_Filename = Get_input("Please Enter The Proxy Filename (Defaults to master.txt): ", str)
	if not Proxy_Filename:
		Proxy_Filename = "master.txt"
	system("title Proxy Checker V_1.0")	


	#Gets Method Type
	Method = Get_input("Please Enter The Method [https, socks4, socks5] (Defaults to https): ", str)
	if not Method:
		Method = "https"
	system("title Proxy Checker V_1.0")


	#Gets timeout
	Timeout = Get_input("Please Enter The Timeout (Defaults to 30): ", int)
	if not Timeout:
		Timeout = 30
	system("title Proxy Checker V_1.0")	



	#Gets Threadcount
	Threadcount = Get_input("Please Enter The Threadcount (Defaults to 200): ", int)
	if not Threadcount:
		Threadcount = 200
	system("title Proxy Checker V_1.0")	


	#Run Program
	Check_Proxies(server=Server, filename=Proxy_Filename, method=Method, timeout=Timeout, threadcount=Threadcount)