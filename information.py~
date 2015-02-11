#information
from counter import counter
import time
import getpass
from carrierlist import carrierlist

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

#Makes an arraylist of arraylists that contains the stops and information
nextdate = True
stoplist = []
while nextdate:

	day = raw_input("Please enter day of the week for reminder 0(Monday)-6(sunday): ")
	time = raw_input("Please enter 24-hour time of the day for reminder hh:mm:ss: ")
	direction = raw_input("Eastbound or Westbound departure?: ")
	stop = raw_input("Stadium, Coffman, or Westbank?: ")
	keepgoing = raw_input("Do you want to add another date, Yes or No?: ")
	stoplist.append((day,time,direction,stop))	
	if keepgoing == "No":
		nextdate = False

	


counter(toaddress, fromaddress, password, username, stoplist)
