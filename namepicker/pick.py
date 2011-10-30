#!/usr/bin/python
import sys, random, time, os

def print_usage_exit():
	sys.exit('Usage: ./%s filename [seed]' % (os.path.basename(sys.argv[0]),))

def main():
	seed = int(time.time()*1000)
	if len(sys.argv) < 2:
		print_usage_exit()
	elif len(sys.argv) == 3 and not sys.argv[2].isdigit():
		print_usage_exit()
	elif len(sys.argv) > 3:
		print_usage_exit()
	else:
		# user input was ok, extract parameters
		participants_file = sys.argv[1]
		if not os.path.isfile(participants_file):
			print "File not found: %s" % (participants_file,)
			print_usage_exit()
		# seed is optional
		if(len(sys.argv) == 3):
			seed = int(sys.argv[2])

	random.seed(seed)
	winner = random.choice(open(participants_file,'r').read().strip().split('\n'))
	print "Winner was: %s (using seed: %d)" % (winner, seed)

if __name__ == "__main__":
	main()
