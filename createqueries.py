
#value, a numer and we return a value between [0,1] depeding on value 
def capitallossqeuery1(value):
	threshold = 10000
	if value == 0:
		return 1
	else:
		val = 1 - (vlaue/threshold) if 1 - (vlaue/threshold)  > 0 else 0
		return val 

def capitallossqeuery2(value):
	threshold = 10000
	val = vlaue/threshold if (vlaue/threshold)  < 1 else 1
	return val 

def capitallossqeuery3(value):
	if value == 0:
		return 1
	else:
		return 1 - (vlaue/threshold)

def agexhourqeuery1(value):
	threshold = 10000
	if value[1] <= 16:
		return 0
	else:
		
		return val 

def agexhourqeuery1(value):
	threshold = 10000
	val = vlaue/threshold if (vlaue/threshold)  < 1 else 1
	return val 