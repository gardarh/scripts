#!/usr/bin/python
import sys, os, json, pprint

def print_usage_exit():
	sys.exit("Usage: ./%s file1.json file2.json" % (os.path.basename(sys.argv[0]),))

def printStack(stack):
	print " *** Stack: %s ***" % (' > '.join(stack),)

def compare_nodes(n1, n2, stack):
	substack = list(stack)
	if(type(n1) != type(n2)):
		print "Nodes have different type, comparison makes no sense"
		print
	elif(type(n1) == dict):
		if n1 != n2:
			printStack(stack)
		n1_keyset = set(n1.keys())
		n2_keyset = set(n2.keys())
		if n1_keyset != n2_keyset:
			n1_exclusive = n1_keyset - n2_keyset
			n2_exclusive = n2_keyset - n1_keyset
			if(len(n1_exclusive) > 0):
				print "Node 1 has the following keys node 2 doesn't: %s" % (', '.join([str(item) for item in n1_exclusive]),)
				print
			if(len(n2_exclusive) > 0):
				print "Node 2 has the following keys node 1 doesn't: %s" % (', '.join([str(item) for item in n2_exclusive]),)
				print
		for key in n1_keyset.intersection(n2_keyset):
			if n1[key] != n2[key]:
				print "Key %s is different between nodes ... going deeper" % (key,)
				print
				substack.append(key)
				compare_nodes(n1[key],n2[key],substack)
	elif(type(n1) == list):
		if n1 != n2:
			printStack(stack)
			print "Lists differ, length(node1)=%d, length(node1)=%d" % (len(n1), len(n2))
			print "Node 1:"
			print n1
			print "Node 2:"
			print n2
			print
	else:
		if n1 != n2:
			printStack(stack)
			print "Node 1 has different value than node 2 (%s - %s)" % (n1,n2)
			print

def main():
	if len(sys.argv) != 3:
		print_usage_exit()
	file1 = sys.argv[1]
	file2 = sys.argv[2]
	try:
		d1 = json.loads(open(file1,'r').read())
		d2 = json.loads(open(file2,'r').read())
	except Exception,e:
		print "Could not load json, error: %s" % (str(e),)
		print_usage_exit()

	print "Comparing %s (node 1) and %s (node 2)" % (file1, file2)
	compare_nodes(d1,d2,['root'])
	
if __name__ == "__main__":
	main()
