#counter
#Counts the time, and sends texts when time is reached
from NexTrain import run
from datetime import datetime
def counter(toaddress, fromaddress, password, username, stoplist):

	#Infinite looping checking and sending when the time is correct
	while True:
		for i in stoplist:
			day = datetime.today().weekday()
			if day == int(i[0]):
				done = True
				while done:
					currenttime = datetime.now()
					currenttime = currenttime.strftime("%H:%M:%S")
					if (currenttime == i[1]):
						run(toaddress,fromaddress,password,username,i[2],i[3])
						done = False
