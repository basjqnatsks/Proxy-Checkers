import os
from urllib.request import Request, urlopen
import urllib
import zipfile
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.command import Command
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
class chrome:
	def __new__(cls, driver_version='76.0.3809.126', headless=None, proxies=None, script=None, location=None, Desired_Capabilities=None, pageLoadStrategy=None, roblox_schemes=None, useragent=None, userdata=None):
		cls.__init__(cls)



		cls.driver_version = driver_version




		cls.Check_And_install_Chrome_Driver(cls)
		cls.chrome(cls, headless, proxies, script, location, Desired_Capabilities, pageLoadStrategy, roblox_schemes, useragent, userdata)
		return cls.var
	def __init__(self, driver_version='74.0.3729.6', headless=None, proxies=None, script=None, location=None, Desired_Capabilities=None, pageLoadStrategy=None, roblox_schemes=None, useragent=None, userdata=None):
		self.headless_JS = """
		Object.defineProperty(navigator, 'webdriver', {
			get: () => false,
		});
		Object.defineProperty(navigator, 'languages', {
			get: () => ['en-US', 'en'],
		});
		Object.defineProperty(navigator, 'plugins', {
			get: () => [1, 2, 3, 4, 5],
		});
		window.chrome = {
			runtime: {},
		};

	"""

		self.JS = """
		Object.defineProperty(navigator, 'webdriver', {
			get: () => false,
		});
	"""

	def Check_And_install_Chrome_Driver(self):
		driver_version = self.driver_version

		#Searching For Chromedriver Directory
		DriverLocation = os.path.isdir("C:\\Users\\Public\\chromedriver")
		if DriverLocation is False:
			#Make Dir For Driver
			os.mkdir("C:\\Users\\Public\\chromedriver")

		#Searching For Chromedriver Version Directory
		SpecificDriverLocation = os.path.isdir("C:\\Users\\Public\\chromedriver\\" + str(driver_version))
		if SpecificDriverLocation is False:
			#Make Dir For Version Driver
			os.mkdir("C:\\Users\\Public\\chromedriver\\" + str(driver_version))

		#Searching For Chromedriver Version EXE
		SpecificDriverFile = os.path.isfile("C:\\Users\\Public\\chromedriver\\" + str(driver_version) +"\\chromedriver.exe") 
		if SpecificDriverFile is False:
			#Download Chrome Driver File
			try:
				urllib.request.urlretrieve("http://chromedriver.storage.googleapis.com/" + str(driver_version) +"/chromedriver_win32.zip", "C:\\Users\\Public\\chromedriver\\" + str(driver_version) +"\\chromedriver.zip")
			except TypeError:#User Messed Up
				raise ValueError("Wrong version Choice For Chrome Class Driver")
			else:
				#Managing Zip
				zip_ref = zipfile.ZipFile("C:\\Users\\Public\\chromedriver\\" + str(driver_version) +"\\chromedriver.zip", 'r')
				zip_ref.extractall("C:\\Users\\Public\\chromedriver\\" + str(driver_version))
				zip_ref.close()
				os.remove("C:\\Users\\Public\\chromedriver\\" + str(driver_version) +"\\chromedriver.zip")













	#sending Javascript file through POST in add_script()
	def send(self, driver, cmd, params={}):
		resource = "/session/%s/chromium/send_command_and_get_result" % driver.session_id
		url = driver.command_executor._url + resource
		body = json.dumps({'cmd': cmd, 'params': params})
		response = driver.command_executor._request('POST', url, body)
		return response.get('value')
	def add_script(self, driver, script):
		self.send(self, driver, "Page.addScriptToEvaluateOnNewDocument", {"source": script})


	def debug(self):
		return self.var
	def chrome(self, headless : bool, proxies : str, script : str, location : str, Desired_Capabilities : bool, pageLoadStrategy : bool, roblox_schemes : bool, useragent : str, userdata : str):
		WebDriver.add_script = self.add_script
		chrome_options = webdriver.ChromeOptions()
		chrome_options.add_argument('--mute-audio')
		if userdata:
			chrome_options.add_argument('--user-data-dir=' + userdata)
		if useragent != None:
			chrome_options.add_argument('----user-agent='+ useragent)
		else:
			chrome_options.add_argument('----user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36')

		if Desired_Capabilities:
			capa = DesiredCapabilities.CHROME
			if pageLoadStrategy:
				capa["pageLoadStrategy"] = "none"
		if headless:
			chrome_options.add_argument("--headless")
		if proxies != None:
			chrome_options.add_argument('--proxy-server=' + str(proxies))
		if roblox_schemes == 't':
			prefs = {"protocol_handler.excluded_schemes":{"roblox-player":False,"roblox-studio":False}}
			chrome_options.add_experimental_option("prefs",prefs)
		if location:
			chrome_options.binary_location = location
		chromedrivers = "C:\\Users\\Public\\chromedriver\\" + str(self.driver_version) +"\\chromedriver.exe"
		if Desired_Capabilities:
			self.var = webdriver.Chrome(chromedrivers, desired_capabilities=capa, chrome_options=chrome_options)
			if headless:
				self.add_script(self, self.var, self.headless_JS)

			else:
				self.add_script(self, self.var, self.JS)
		else:
			self.var = webdriver.Chrome(chromedrivers, chrome_options=chrome_options)
			if headless:
				self.add_script(self, self.var, self.headless_JS)
			else:
				self.add_script(self, self.var, self.JS)
		if script !=None:
			self.add_script(self, self.var, script)
		return self.var