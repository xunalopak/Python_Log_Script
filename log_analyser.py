import re
import time
import sys
import requests
import os

def analyse_log(filename):
    new_line = ""

    with open(filename, 'r') as log:
        while True:
            new_line = log.readline()
            if not new_line:
                time.sleep(1)
                log.seek(log.tell())
            else:
                print(new_line)


def initialisation(text):
    namefile = "log.txt"
    
    try:
        with open(namefile, 'xw') as logfile:
            logfile.write(text)
            pass
    except:
        print("File already create\nPut information in the file...")
        with open(namefile, "w") as logfile:
            logfile.write(text)
    return namefile

print (sys.argv[1])
resp = requests.get(sys.argv[1])
print(resp.text)

filename = initialisation(resp.text)
# analyse_log(filename)

