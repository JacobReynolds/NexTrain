#TimeCounter
from NexTrain import run
import time
import getpass
from carrierlist import carrierlist
from trainlist import trainlist

#Gmail login details
username = raw_input("Please enter Gmail address: ")
password = getpass.getpass("Please enter Gmail password: ")
fromaddress = username
toaddress = raw_input("Please enter cellphone number or email: ")
if not '@' in toaddress:
	print("Please enter cellphone carrier(case sensitive) from list: ")
	#Prints list of carriers
	for key in carrierlist.keys():
	    print(key)
	carrier = raw_input("Please enter cellphone carrier: ")

	#Adds carrier address to phone number to be e-mailed
	for key,value in carrierlist.items():
	    if key == carrier:
		toaddress = toaddress + value


#Train preference details
direction = raw_input("Eastbound or Westbound departure?: ")



run(toaddress, fromaddress, password, username)
