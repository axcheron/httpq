from colorama import Style, Fore, Back, init
import argparse
import requests
import urllib3
import socket
import os.path
import bs4

# Disable SSL/TLS Warnings
urllib3.disable_warnings()
# Reset Colorama
init(autoreset=True)

http_code = {
    # Informational
    100: 'Continue', 101: 'Switching Protocols', 102: 'Processing', 
    # Success
    200: 'OK', 201: 'Created', 202: 'Accepted', 203: 'Non-authoritative Information', 204: 'No Content', 
    205: 'Reset Content', 206: 'Partial Content', 207: 'Multi-Status', 208: 'Already Reported', 226: 'IM Used', 
    # Redirect
    300: 'Multiple Choices', 301: 'Moved Permanantly', 302: 'Found', 303: 'See Other', 304: 'Not Modified', 
    305: 'Use Proxy', 307: 'Temporary Redirect', 308: 'Permanant Redirect', 
    # Client Error
    400: 'Bad Requests', 401: 'Unauthorized', 402: 'Payment Required', 403: 'Forbidden', 404: 'Not Found', 
    405: 'Method Not Allowed', 406: 'Not Acceptable', 407: 'Proxy Authentication Required', 408: 'Request Timeout', 
    409: 'Conflict', 410: 'Gone', 411: 'Length Required', 412: 'Preconditions Failed', 413: 'Payload Too Large', 
    414: 'Request-URI Too Long', 415: 'Unsupported Media Type', 416: 'Requested Range Not Satisfiable', 417: 'Excpectation Failed', 
    418: 'I\'m a teapot', 421: 'Misdirected Request', 422: 'Unprocessable Entity', 423: 'Locked', 424: 'Failed Dependency', 
    426: 'Upgrade Required', 428: 'Precondition Required', 429: 'Too Many Requests', 431: 'Request Header Fields Too Large', 
    444: 'Connection Closed Without Response', 451: 'Unvailable For Legal Reasons', 499: 'Client Closed Request', 
    # Server Error
    500: 'Internal Server Error', 501: 'Not Implemented', 502: 'Bad Gateway', 503: 'Service Unavailable', 504: 'Gateway Timeout', 
    505: 'HTTP Version Not Supported', 506: 'Variant Also Negociates', 507: 'Insufficient Storage', 508: 'Loop Detected', 
    510: 'Not Extended', 511: 'Network Authentication Required', 599: 'Network Connect Timeout Error'
}

def get_status(url, redirect, timeout):
    try:
        r = requests.get(url, timeout=timeout, allow_redirects=redirect, verify=False) 
        s = r.status_code
        c = bs4.BeautifulSoup(r.text, features='html.parser')
        
        try:
            t = Fore.LIGHTMAGENTA_EX + c.title.string
        except:
            t = Fore.RED + "none"

        print(Fore.RED + "[+] " + Fore.WHITE + r.url, end='')

        if s in http_code:
            print(" - %d (%s) - %s" % (s, http_code[s], t))
        else:
            print(" - %d" % s)

    except requests.RequestException:
        pass

def httpq(dom_list, redirect, timeout):
    if os.path.isfile(dom_list):
        fh = open(dom_list, 'r')
        domains = fh.read()
        domains = domains.rsplit()

        for dom in domains:
            get_status(dom, redirect, timeout)

    else:
        print(Fore.RED + "[-] Invalid file.")
        exit(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check HTTP(S) Status Code for Domain(s).')

    # Add arguments
    parser.add_argument("domains", help="File with domains list", type=str)
    parser.add_argument("-r", "--redirect", help="Check redirection (default = False)", action="store_true", default=False)
    parser.add_argument("-t", "--timeout", help="Change HTTP timeout (default = 5 sec.)", action="store", default=5)

    args = parser.parse_args()

    try:
        timeout = int(args.timeout)
    except ValueError:
        print(Fore.RED + "[-] Invalid value for 'timeout'.")
        exit(1)

    httpq(args.domains, args.redirect, timeout)
