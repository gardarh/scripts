#!/usr/bin/python
import os
import sys
import socket
import requests

def print_usage_exit():
	sys.exit('Usage: ./%s ip [port]' % (os.path.basename(sys.argv[0]),))

def main():
    sockinfo = None
    proto = 'https'
    port = 443 if proto == 'https' else 80
    if len(sys.argv) < 2:
            print_usage_exit()
    else:
        if len(sys.argv) > 2 and sys.argv[2].isdigit():
            port = int(sys.argv[2])
        sockinfo = socket.getaddrinfo(sys.argv[1], port, socket.AF_INET, 0, socket.IPPROTO_TCP)
    if not sockinfo:
        print "Could not resolve host"
        print_usage_exit()

    ip = sockinfo[0][4][0]
    addr = "%s://%s:%d/" % (proto, ip, port)
    #headers = {}
    #hostname = ip# 'mcnulty.stefja.net'
    #headers = {'Host': hostname}

    print "Asking for %s ..." % (addr,)
    r = requests.get(addr, verify=False)
    print
    print "HTTP CODE: %d" % (r.status_code,)
    print "----- REQUEST -------"
    hprint(r.request.headers)
    print
    print "----- RESPONSE -------"
    hprint(r.headers)
    print


def hprint(data):
    for (key,value) in data.iteritems():
        print "%s: %s" % (key, value)

if __name__ == "__main__":
	main()

