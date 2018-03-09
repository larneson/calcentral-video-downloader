import datetime
import getpass


USERNAME = "aemartyn"
PASSWORD = getpass.getpass()
OUTPUT_LOCATION = "."
LIMIT_RATE = ""

def get_semester(day=None):
	if day is None:
		day = datetime.date.today()
	if day.month in range(1, 6):
		season = "spring"
	elif day.month in range(6, 8):
		season = "summer"
	else:
		season = "fall"
	return "{}-{}".format(season, day.year)

SEMESTER = get_semester() #i.e fall-2017