import random

import string

import csv

import progressbar

def getcount():

	rownums = raw_input("How many fake email addresses?: ")	try:

		rowint = int(rownums)

		return rowint

	except ValueError:

		print("Please enter an integer value")

		return getcount()

def makeEmail():

	extensions = ['com','net','org','gov']

	domains = ['gmail','yahoo','comcast','verizon','charter','hotmail','outlook','frontier']

	winext = extensions[random.randint(0,len(extensions)-1)]

	windom = domains[random.randint(0,len(domains)-1)]

	acclen = random.randint(1,20)

	winacc = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(acclen))

	finale = winacc + "@" + windom + "." + winext

	return finale

howmany = getcount()

counter = 0

emailarray = []

print("Creating email addresses...")

print("Progress: ")

prebar = progressbar.ProgressBar(maxval=int(howmany))

for i in prebar(range(howmany)):

	while counter <= howmany:

		emailarray.append(str(makeEmail()))

		counter = counter+1

		prebar.update(i)

	

print("Creation completed.")

filename = raw_input("name your file: ")

print ("Progress: ")

bar = progressbar.ProgressBar(maxval=int(howmany))

emailfile = open(str(filename), 'wa')

aa = csv.writer(emailfile)

for emailaddr in bar(emailarray):

	aa.writerow([emailaddr])

	bar.update()

emailfile.close()

print ("File '" + filename + "' created.")
