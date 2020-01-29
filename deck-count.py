import sys
import re

def main(argv):
	tempsum = 0
	with open(argv[1]) as inputfile:
		for line in inputfile:
			print(line)
			cardnum = re.search("^[0-9]", line)
			tempsum += int(cardnum.group(0))
	print("total cards: %s" % tempsum)

main(sys.argv)