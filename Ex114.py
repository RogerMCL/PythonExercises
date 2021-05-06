# EXERCÍCIO 114:

import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[031mERRO! O site não está acessível!\033[m')
else:
    print('\033[032mO site está acessível!\033[m')
