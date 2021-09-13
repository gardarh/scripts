#!/usr/bin/python
import sys, os, json

def print_usage_exit():
    usage = [
            'Usage: ./%s <filename.json>' % (os.path.basename(sys.argv[0]),),
            '',
            'File should contain a json array with terms to convert. Words are',
            'converted from camelCase to snake_case',
            ]
    sys.exit('\n'.join(usage))

def main():
    if len(sys.argv) < 2:
        print_usage_exit()
    else:
        # user input was ok, extract parameters
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print("File not found: %s" % (filename,))
            print_usage_exit()
        with open(filename, 'r') as fn:
            words = json.load(fn)
    
    result = {}
    for word in words:
        cur_out = ''
        for char in word:
            if char.isupper():
                cur_out += '_' + char.lower()
            else:
                cur_out += char
        result[word] = cur_out


    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
