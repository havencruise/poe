#!/usr/bin/env python
import sys, re
import SimpleHTTPServer, SocketServer

ipregex = re.compile(r"""^(?:
            (?P<addr>\d{1,3}(?:\.\d{1,3}){3}         # IPv4 address
            ):)?(?P<port>\d+)$""", re.X)
NAME = sys.argv[0]

def usage(name):
    print 'Usage:'
    print '  %s <ip-addr>:<port>' % name
    print '  Example: %s 127.0.0.1:8000' % name
    print '\n'


def run(addr, port):
    handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer((addr, port), handler)
    httpd.serve_forever()


if __name__ == "__main__":
    addr = ''
    port = '8000'
    if len(sys.argv[1:]) > 0:
        m = re.match(ipregex, sys.argv[1])
        if m is None:
            usage(NAME)
            sys.exit(2)
        addr, port = m.groups()
    print 'Running server on %s, on port %s' % (addr or 'localhost', port)
    run(addr, int(port))

