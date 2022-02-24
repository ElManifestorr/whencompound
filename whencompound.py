
# Introduction to gather variables


print('What is your starting amount?')
starter = int(input()) # a is for the amount to start with
a = starter

print('How many days would you like to calculate for?')
days = int(input()) #amount of days you'd like to compound

print('& finally, at what percent daily return?')
percentincrease = float(input())
dailyYield = float(percentincrease / 100)


sixtimesDaily = days * 6
while sixtimesDaily != 0:
	a = a * float(1 + (dailyYield / 6))
	if sixtimesDaily == 1:
		print('compounding 6 times daily for ' + str(days) + ' days compounds to: ' + str(a))
	sixtimesDaily = sixtimesDaily - 1
	continue
twiceDaily = days * 2
a = starter
while twiceDaily != 0:
	a = a * (1 + float(dailyYield / 2))
	if twiceDaily == 1:
		print('compounding 2 times daily for ' + str(days) + ' days compounds to: ' + str(a))
	twiceDaily = twiceDaily - 1
	continue
daily = days * 1
a = starter
while daily != 0:
	a = a * float(1 + dailyYield)
	if daily == 1:
		print('compounding 1 time daily for ' + str(days) + ' days compounds to: ' + str(a))
	daily = daily - 1
	continue
bidaily = days // 2
a = starter
while bidaily != 0:
	a = a * (1 + float(dailyYield * 2))
	if bidaily == 1:
		print('compounding every other day for ' + str(days) + ' days compounds to: ' + str(a))
	bidaily = bidaily - 1
	continue 
weekly = days // 7
a = starter
while weekly != 0:
	a = a * (1 + float(dailyYield * 7))
	if weekly == 1:
		print('compounding once weekly for ' + str(days) + ' days compounds to: ' + str(a))
	weekly = weekly - 1
	continue
