import requests
import threading
import time
import os
import math
from queue import Queue
#pip install -U requests[socks]
class Check_Proxies(object):
	def __init__(self, server: str = "google.com", filename: str = "master.txt", method: str = "https", timeout: int = 30, threadcount: int = 200) -> None:
		#inits
		#time counter
		self.LAST_ = time.time()
		self.start_time = time.time()
		#Proxy File Name
		self.filename = filename
		#server Site
		self.Server = server
		#Method Type
		self.method = method
		#timeout
		self.timeout = timeout
		#thread amount
		self.threadcount = threadcount
		#static Methods
		self.Queued_iteation_count = 0
		self.ActiveThreadcountInsideFunc = 0
		#length of proxy File
		self.socket = ""
		self.validProxies = []
		self.failedProxies = []
		self.threadedArray = []
		#verifications
		#temp method list
		SupportedMethods = ["https", "socks5", "socks4", "http"]
		#checking method 
		if self.method not in SupportedMethods:
			raise IOError("Wrong Method")
		del SupportedMethods
		if self.method != "https" or self.method != "http":
			self.socket = self.method + "://"
			self.method = "https"
		#checking if timeout is number
		try:
			self.timeout = float(self.timeout)
		except:
			raise IOError("Timeout Not a Number")

		#checking threadcount if int
		try:
			self.threadcount = int(self.threadcount)
		except:
			raise IOError("Threadcount Not a Number")
		#readfile 
		self.proxies = self.readfile(self.filename)
		#Active Thread Counter
		self.TaskLength = len(self.proxies)
		self.SettingTaskQueue()
	#reads file
	def readfile(self, FileName: str) -> []:
		with open(FileName, "rb") as f:
			return f.read().decode("ISO-8859-1").replace("\r", "").split("\n")
	#updates os module
	def updateTitle(self, Iter: int, ThreadCount: int, FinalLength: int, WorkingAccountsLength: int, FailedAccountLength: int) -> None:
		os.system('title ' + 'Active threads [' + str(ThreadCount)  + ']   Working [' + str(WorkingAccountsLength) + ']' + '   Failed [' + str(FailedAccountLength) + ']   Progress [' + str(Iter) + '/' + str(FinalLength) + ']   Time elapsed [' + str((math.ceil((time.time() - self.start_time)*1000))/1000) + ']')	
	#checker
	def check(self, Iter: int, Proxy: str) -> None:
		#threadcounter
		self.ActiveThreadcountInsideFunc += 1
		#Updates Os Every 1000 threads
		if (time.time() - self.LAST_) > 1:
			self.LAST_ = time.time()
			self.updateTitle(Iter, self.ActiveThreadcountInsideFunc, self.TaskLength, len(self.validProxies), len(self.failedProxies))
		try:
			r = requests.delete(self.method+"://"+self.Server, proxies={self.method:self.socket+Proxy}, timeout=self.timeout, headers={'Content-Type': 'application/json'})
		except:
			self.failedProxies.append(Proxy)
		else:
			self.validProxies.append(Proxy)
			with open("socks.txt", "a") as cc:
				cc.write(self.socket + Proxy + '\n')
		#threadcounter
		self.ActiveThreadcountInsideFunc -= 1
	def SettingTaskQueue(self):
		def threader():
			while True:
				A = queue.get()
				self.check(A[0], A[1])
				queue.task_done()
		queue = Queue()
		for null in range(self.threadcount):
			t = threading.Thread(target=threader)
			t.daemon = True
			self.threadedArray.append(t)
			t.start()
		for worker in range(len(self.proxies)):
			Temp_Get_Array = [worker, self.proxies[self.Queued_iteation_count]]
			queue.put(Temp_Get_Array)

			self.Queued_iteation_count += 1

		for i in range(self.threadcount):
			queue.put(None)
		for t in self.threadedArray:
			t.join()
		print('Entire job took: ',time.time() - self.start_time)
