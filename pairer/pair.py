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
    orig_list = open(participants_file,'r').read().strip().split('\n')
    permutated = list(orig_list)
    while is_someone_points_to_self(orig_list, permutated):
        random.shuffle(permutated)

    print "Final list:"
    for i in xrange(len(orig_list)):
        print "%s -> %s" % (orig_list[i], permutated[i])

def is_someone_points_to_self(list1, list2):
    for i in xrange(len(list1)):
        if list1[i] == list2[i]:
            return True
    return False
        


if __name__ == "__main__":
    main()
