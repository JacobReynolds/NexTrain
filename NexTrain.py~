#NexTrain
import smtplib
from lxml import html
import requests
from datetime import datetime
from trainlist import westtrainlist
from trainlist import easttrainlist


def run(toaddress, fromaddress, password, username, direction, stop):
	
	#Train preference details
	if direction == "Eastbound":
		for key,value in easttrainlist.items():
			if key == stop:
				website = value
	elif direction == "Westbound":
		for key,value in westtrainlist.items():
			print(key)
			if key == stop:
				website = value
	else:
		print("Invalid input")
		return
	#Gets the next time from the NexTrip website
	page = requests.get(website)
	tree = html.fromstring(page.text)
	time = tree.xpath('//*[@id="NexTripControl1_NexTripResults1_lblNextDepartureText"]/b[2]/text()')
	msg = ("The next " + direction + " train from " + stop + " leaves in " + time[0] + "\nSent at: " + str(datetime.now()))

	print(msg)

	#Sends message using Gmail servers
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddress,toaddress,msg)
	server.quit()
	print("Message sent")
